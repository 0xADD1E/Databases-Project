import logging
from django.shortcuts import render
from django.http import HttpResponseServerError


def encode_image(image: bytes, mime: str):
    from base64 import b64encode
    if image is None:
        return None
    else:
        return f"data:{mime};base64,{b64encode(image).decode('UTF-8')}"


def pokemon_view(request):
    from .models import Pokemon
    from math import ceil
    from collections import namedtuple
    from django.db import connection
    log = logging.getLogger('pokemon_view')
    CARDS_PER_PAGE = 18

    pagination_item = namedtuple('Page', ['number', 'display', 'is_active'])
    page = int(request.GET.get('page', '0'))
    total_pages = int(ceil(Pokemon.objects.count() / 18))
    display_pages = [pagination_item(number=n, display=n + 1, is_active=(n == page))
                     for n in range(total_pages)
                     if abs(page - n) < 7]

    with connection.cursor() as cursor:
        pokemon = namedtuple('Pokemon', ['name', 'pokedex_id', 'image'])
        pokemon_list = []
        cursor.execute("""
        SELECT frontend_pokemon.pokedex_id AS pokedex_id,
            frontend_pokemon.name AS name,
            first_media.data AS image,
            first_media.mime_id AS mime
        FROM frontend_pokemon
        LEFT JOIN (
            SELECT *
            FROM frontend_media
            GROUP BY frontend_media.of_id
            ) AS first_media ON first_media.of_id = frontend_pokemon.pokedex_id
        ORDER BY frontend_pokemon.pokedex_id
        LIMIT %s OFFSET %s""", [CARDS_PER_PAGE, CARDS_PER_PAGE * page])
        for (pokedex_id, name, image, mime) in cursor.fetchall():
            image_encoded = encode_image(image, mime)
            pokemon_list.append(pokemon(name=name,
                                        pokedex_id=pokedex_id,
                                        image=image_encoded))

        return render(request, 'pokemon_list.html',
                      {'pokemon_list': pokemon_list, 'pages': display_pages, 'max': total_pages - 1})


def searchie_boi(request):
    import json
    from .models import Pokemon
    pokemon_names = json.dumps([{'id': x.pokedex_id, 'title': x.name}
                                for x in Pokemon.objects.all()])

    return render(request, 'searchieboi.html', {'pokemon_names': pokemon_names})


def pokemon_info(request):
    import json
    from django.http import HttpResponse, HttpResponseBadRequest
    from .models import Pokemon
    pokemon_name = request.GET.get('for', 'Pikachu')

    pokemon = Pokemon.objects.get(name=pokemon_name)
    image = pokemon.media_set.first()
    types = pokemon.pokemontype_set.all()
    abilities = pokemon.pokemonability_set.all()

    result = {
        'name': pokemon.name,
        'id': str(pokemon.pokedex_id).zfill(3),
        'height': pokemon.height,
        'weight': pokemon.weight,
        'types': [t.pokemon_type.name for t in types],
        'abilities': [t.pokemon_ability.name for t in abilities],
        'image': encode_image(image.data, image.mime)
    }
    return HttpResponse(json.dumps(result), content_type='application/json')


def matchup_uploader(request):
    from .models import Type, TypeMatchup
    from django import forms
    import csv
    log = logging.getLogger('matchup_import')

    class MatchupForm(forms.Form):
        matchups = forms.FileField()
    if request.method == 'POST':
        form = MatchupForm(request.POST, request.FILES)
        lines = [x.decode('UTF-8')
                 for x in request.FILES['matchups'].readlines()[1:]]
        rd = csv.reader(lines)
        for s, o, m in rd:
            self_t, created = Type.objects.get_or_create(name=s)
            if created:
                self_t.save()
                log.info(f'Added type {self_t}')
            other_t, created = Type.objects.get_or_create(name=o)
            if created:
                other_t.save()
                log.info(f'Added type {other_t}')

            matchup, created = TypeMatchup.objects.get_or_create(this=self_t,
                                                                 other=other_t)

            matchup.effectiveness_multiplier = m
            matchup.save()
            if created:
                log.info(f'Added matchup {matchup}')
        for self_t in Type.objects.all():
            for other_t in Type.objects.all():
                matchup, created = TypeMatchup.objects.get_or_create(this=self_t,
                                                                     other=other_t)
                if created:
                    matchup.effectiveness_multiplier = 1
                    matchup.save()
                    log.info(f'Added matchup {matchup}')
    else:
        form = MatchupForm()
    return render(request, 'upload.html', {'form': form, 'is_valid': form.is_valid(), 'endpoint': 'matchup'})


def typechart(request):
    from .models import Type, TypeMatchup
    log = logging.getLogger('matchup_import')
    types = []
    matchups = []
    for t in Type.objects.order_by('name'):
        typename = t.name.title()
        types.append(typename)
        matchups.append([])
        matchups[-1].append(('', typename))
        for m in TypeMatchup.objects.filter(this=t).order_by('other'):
            num = m.effectiveness_multiplier
            if num == 2.0:
                matchups[-1].append(('positive', '2x'))
            elif num == 1.0:
                matchups[-1].append(('', '-'))
            elif num == 0.5:
                matchups[-1].append(('negative', '1/2x'))
            elif num == 0.0:
                matchups[-1].append(('negative', '0x'))

    log.debug(matchups)
    return render(request, 'typechart.html', {'types': types, 'matchups': matchups})


def kalos_uploader(request):
    from .models import Pokemon, PokemonType, Media, MIMEType, Type, Ability, PokemonAbility
    import json
    from requests import get
    from django import forms
    log = logging.getLogger('kalos_import')

    class KalosForm(forms.Form):
        kalos = forms.FileField()

    if request.method == 'POST':
        form = KalosForm(request.POST, request.FILES)
        png = MIMEType.objects.get(mime_string='image/png')
        for pkmn in json.load(request.FILES['kalos']):
            new, created = Pokemon.objects.get_or_create(pokedex_id=pkmn['id'])
            if created:
                new.name = pkmn['name']
                new.weight = pkmn['weight']
                new.height = pkmn['height']
                new.gender_distribution = 0
                new.legendary = False
                new.save()
                log.debug(f'Added pokemon {new.name}')
            thumb, created = Media.objects.get_or_create(filename=f'{new.name}_thummbnail.png',
                                                         mime=png,
                                                         of=new)
            if created:
                thumb.data = get(pkmn['ThumbnailImage']).content
                thumb.save()
                log.debug(f'Saved thumbnail for {new.name}')
            for pkmnType in pkmn['type']:
                newtype, created = Type.objects.get_or_create(
                    name=pkmnType)
                newtype.save()
                if created:
                    log.info('Added type {}'.format(newtype))
                pkmnType, created = PokemonType.objects.get_or_create(pokemon=new,
                                                                      pokemon_type=newtype)
                pkmnType.save()
                if created:
                    log.debug('Saved Pokemon Type {0} for {1}'.format(pkmnType.pokemon_type,
                                                                      pkmnType.pokemon.name))

            for pkmnAbility in pkmn['abilities']:
                newAbility, created = Ability.objects.get_or_create(
                    name=pkmnAbility)
                newAbility.save()
                if created:
                    log.info('Added ability: {}'.format(newAbility))
                pkmnAbility, created = PokemonAbility.objects.get_or_create(pokemon=new,
                                                                            pokemon_ability=newAbility)
                pkmnAbility.save()
                if created:
                    log.debug('Saved Pokemon Ability {0} for {1}'.format(pkmnAbility.pokemon_ability,
                                                                         pkmnAbility.pokemon.name))
    else:
        form = KalosForm()
    return render(request, 'upload.html', {'form': form, 'is_valid': form.is_valid(), 'endpoint': 'kalos'})
