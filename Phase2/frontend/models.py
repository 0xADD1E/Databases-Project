from django.db import models


class Pokemon(models.Model):
    def __str__(self):
        return '{}'.format(self.name)
    pokedex_id = models.IntegerField(primary_key=True)
    name = models.TextField(default='')
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    gender_distribution = models.IntegerField(default=0)
    legendary = models.BooleanField(default=False)


class Ability(models.Model):
    def __str__(self):
        return '{}'.format(self.name)
    name = models.TextField(primary_key=True)


class PokemonAbility(models.Model):
    def __str__(self):
        return '{}: {}'.format(self.pokemon, self.pokemon_ability)
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE)
    pokemon_ability = models.ForeignKey(Ability,
                                        on_delete=models.CASCADE)


class PokemonEvolution(models.Model):
    def __str__(self):
        return '{} => {}'.format(self.base, self.evolution)
    base = models.ForeignKey(Pokemon,
                             on_delete=models.CASCADE,
                             related_name='evolves_to')
    evolution = models.ForeignKey(Pokemon,
                                  on_delete=models.CASCADE,
                                  related_name='evolved_from')


class Type(models.Model):
    def __str__(self):
        return '{}'.format(self.name)
    name = models.TextField(primary_key=True)


class PokemonType(models.Model):
    def __str__(self):
        return '{}: {}'.format(self.pokemon, self.pokemon_type)
    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.CASCADE)
    pokemon_type = models.ForeignKey(Type,
                                     on_delete=models.CASCADE)


class MIMEType(models.Model):
    def __str__(self):
        return '{}'.format(self.mime_string)
    mime_string = models.TextField(primary_key=True)
    friendly_name = models.TextField()
    extension = models.TextField()


class Media(models.Model):
    def __str__(self):
        return '{}'.format(self.filename)
    # django auto-handles INT PK AI fields
    filename = models.TextField()
    data = models.BinaryField(default=b'')
    of = models.ForeignKey(Pokemon,
                           on_delete=models.CASCADE)
    mime = models.ForeignKey(MIMEType,
                             on_delete=models.PROTECT)


class Platform(models.Model):
    def __str__(self):
        return '{}'.format(self.name)
    name = models.TextField(primary_key=True)


class Game(models.Model):
    from datetime import datetime

    def __str__(self):
        return '{}'.format(self.name)
    name = models.TextField(primary_key=True)
    release_date = models.DateField(default=datetime.now)
    platform = models.ForeignKey(Platform,
                                 on_delete=models.PROTECT)


class PokemonAppearance(models.Model):
    def __str__(self):
        return '{}'.format(self.pokemon)
    base_hp = models.IntegerField(default=0)
    base_speed = models.IntegerField(default=0)
    base_attack = models.IntegerField(default=0)
    base_defence = models.IntegerField(default=0)
    base_sp_attack = models.IntegerField(default=0)
    base_sp_defence = models.IntegerField(default=0)

    pokemon = models.ForeignKey(Pokemon,
                                on_delete=models.PROTECT)


class Attack(models.Model):
    def __str__(self):
        return '{}'.format(self.name)
    name = models.TextField(primary_key=True)
    pp = models.IntegerField(default=0)
    power = models.IntegerField(default=0)
    priority = models.IntegerField(default=0)
    accuracy = models.IntegerField(default=0)
    tm_number = models.IntegerField(default=None,
                                    blank=True,
                                    null=True)


class PokemonCanLearn(models.Model):
    def __str__(self):
        return '{}: {}'.format(self.appearance, self.attack)
    at_level = models.IntegerField(default=0)
    appearance = models.ForeignKey(PokemonAppearance,
                                   on_delete=models.CASCADE)
    attack = models.ForeignKey(Attack,
                               on_delete=models.CASCADE)


class TypeMatchup(models.Model):
    def __str__(self):
        return '{} vs {}'.format(self.this, self.other)
    effectiveness_multiplier = models.FloatField(default=0)
    this = models.ForeignKey(Type,
                             on_delete=models.CASCADE,
                             related_name='+')
    other = models.ForeignKey(Type,
                              on_delete=models.CASCADE,
                              related_name='+')


class AttackTypes(models.Model):
    def __str__(self):
        return '{}: {}'.format(self.attack, self.attack_type)
    attack = models.ForeignKey(Attack,
                               on_delete=models.CASCADE)
    attack_type = models.ForeignKey(Type,
                                    on_delete=models.CASCADE)
