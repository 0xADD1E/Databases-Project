from django.db import models


class Pokemon(models.Model):
    pokedex_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    weight = models.FloatField()
    height = models.FloatField()
    gender_distribution = models.IntegerField()
    legendary = models.BooleanField()


class PokemonEvolution(models.Model):
    base = models.ForeignKey(Pokemon,
                             on_delete=models.CASCADE,
                             related_name='evolves_to')
    evolution = models.ForeignKey(Pokemon,
                                  on_delete=models.CASCADE,
                                  related_name='evolved_from')
class Type(models.Model):
    name = models.TextField(primary_key=True)

class PokemonType(models.Model):
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE)
    pokemon_type = models.ForeignKey(Type,
                                     on_delete=models.CASCADE)

class MIMEType(models.Model):
    mime_string = models.TextField(primary_key=True)
    friendly_name = models.TextField()
    extension = models.TextField()


class Media(models.Model):
    # django auto-handles INT PK AI fields
    filename = models.TextField()
    data = models.BinaryField()
    of = models.ForeignKey(Pokemon,
                           on_delete=models.PROTECT)
    mime = models.ForeignKey(MIMEType,
                             on_delete=models.PROTECT)


class Platform(models.Model):
    name = models.TextField(primary_key=True)


class Game(models.Model):
    name = models.TextField(primary_key=True)
    release_date = models.DateField()
    platform = models.ForeignKey(Platform,
                                 on_delete=models.PROTECT)


class PokemonAppearance(models.Model):
    base_hp = models.IntegerField()
    base_speed = models.IntegerField()
    base_attack = models.IntegerField()
    base_defence = models.IntegerField()
    base_sp_attack = models.IntegerField()
    base_sp_defence = models.IntegerField()

    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.PROTECT)
    game = models.ForeignKey(Game,
                             on_delete=models.PROTECT)


class Attack(models.Model):
    name = models.TextField(primary_key=True)
    pp = models.IntegerField()
    power = models.IntegerField()
    priority = models.IntegerField()
    accuracy = models.IntegerField()
    tm_number = models.IntegerField(default=None, blank=True, null=True)


class PokemonCanLearn(models.Model):
    at_level = models.IntegerField()
    appearance = models.ForeignKey(PokemonAppearance,
                                   on_delete=models.CASCADE)
    attack = models.ForeignKey(Attack,
                               on_delete=models.CASCADE)

class TypeMatchup(models.Model):
    effectiveness_multiplier = models.FloatField()
    this = models.ForeignKey(Type,
                             on_delete=models.CASCADE,
                             related_name='+')
    other = models.ForeignKey(Type,
                              on_delete=models.CASCADE,
                              related_name='+')


class AttackTypes(models.Model):
    attack = models.ForeignKey(Attack,
                               on_delete=models.CASCADE)
    attack_type = models.ForeignKey(Type,
                                    on_delete=models.CASCADE)
