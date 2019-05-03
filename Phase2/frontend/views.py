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


def pokemon_info(request):
    import json
    from django.http import HttpResponse, HttpResponseBadRequest
    from .models import Pokemon
    pokemon_name = request.GET.get('for', 'Pikachu')

    pokemon = Pokemon.objects.get(name=pokemon_name)
    image = pokemon.media_set.first()
    types = pokemon.pokemontype_set.all()

    result = {
        'name': pokemon.name,
        'id': pokemon.pokedex_id,
        'types': [t for t in types],
        'image': encode_image(image.data, image.mime)
    }
    return HttpResponse(json.dumps(result), content_type='application/json')


def kalos_uploader(request):
    from .models import Pokemon, PokemonType, Media, MIMEType, Type
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
            newtype = Type(name=pkmn['type'])
            log.info('Added type {}'.format(newtype))
            new = Pokemon.objects.get_or_create(pokedex_id=pkmn['number'],
                                      name=pkmn['name'],
                                      weight=pkmn['weight'],
                                      height=pkmn['height'],
                                      gender_distribution=0,
                                      legendary=False)
            log.info('Added pokemon {}'.format(new[1]))
            thumb = Media.objects.get_or_create(filename='{}_thummbnail.png'.format(new[0]),
                          mime=png,
                          data=get(pkmn['ThumbnailImage']).content,
                          of=new)
            thumb.save()
            log.debug('Saved thumbnail for {}'.format(new[0]))
            pkmnType = PokemonType(pokemon=new,
                                                         pokemon_type=newtype)
            log.debug('Saved Pokemon Type {0} for {1}'.format(pkmnType.pokemon_type,
                                                              pkmnType.pokemon.name))
    else:
        form = KalosForm()
    return render(request, 'upload.html', {'form': form, 'is_valid': form.is_valid()})
