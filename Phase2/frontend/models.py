from django.db import models


class Pokemon(models.Model):
    def __str__(self):
        return f'{self.name}'
    pokedex_id: models.IntegerField = models.IntegerField(primary_key=True)
    name: models.TextField = models.TextField(default='')
    weight: models.FloatField = models.FloatField(default=0)
    height: models.FloatField = models.FloatField(default=0)
    gender_distribution: models.IntegerField = models.IntegerField(default=0)
    legendary: models.BooleanField = models.BooleanField(default=False)


class Ability(models.Model):
    def __str__(self):
        return f'{self.name}'
    name: models.TextField = models.TextField(primary_key=True)


class PokemonAbility(models.Model):
    def __str__(self):
        return f'{self.pokemon}: {self.pokemon_ability}'
    pokemon: models.ForeignKey = models.ForeignKey(Pokemon,
                                                   on_delete=models.CASCADE)
    pokemon_ability: models.ForeignKey = models.ForeignKey(Ability,
                                                           on_delete=models.CASCADE)


class PokemonEvolution(models.Model):
    def __str__(self):
        return f'{self.base} -> {self.evolution}'
    base: models.ForeignKey = models.ForeignKey(Pokemon,
                                                on_delete=models.CASCADE,
                                                related_name='evolves_to')
    evolution: models.ForeignKey = models.ForeignKey(Pokemon,
                                                     on_delete=models.CASCADE,
                                                     related_name='evolved_from')


class Type(models.Model):
    def __str__(self):
        return f'{self.name}'
    name: models.TextField = models.TextField(primary_key=True)


class PokemonType(models.Model):
    def __str__(self):
        return f'{self.pokemon}: {self.pokemon_type}'
    pokemon: models.ForeignKey = models.ForeignKey(Pokemon,
                                                   on_delete=models.CASCADE)
    pokemon_type: models.ForeignKey = models.ForeignKey(Type,
                                                        on_delete=models.CASCADE)


class MIMEType(models.Model):
    def __str__(self):
        return f'{self.mime_string}'
    mime_string: models.TextField = models.TextField(primary_key=True)
    friendly_name: models.TextField = models.TextField()
    extension: models.TextField = models.TextField()


class Media(models.Model):
    def __str__(self):
        return f'{self.filename}'
    # django auto-handles INT PK AI fields
    filename: models.TextField = models.TextField()
    data: models.BinaryField = models.BinaryField(default=b'')
    of: models.ForeignKey = models.ForeignKey(Pokemon,
                                              on_delete=models.CASCADE)
    mime: models.ForeignKey = models.ForeignKey(MIMEType,
                                                on_delete=models.PROTECT)


class Platform(models.Model):
    def __str__(self):
        return f'{self.name}'
    name: models.TextField = models.TextField(primary_key=True)


class Game(models.Model):
    from datetime import datetime

    def __str__(self):
        return f'{self.name}'
    name: models.TextField = models.TextField(primary_key=True)
    release_date: models.DateField = models.DateField(default=datetime.now)
    platform: models.ForeignKey = models.ForeignKey(Platform,
                                                    on_delete=models.PROTECT)


class PokemonAppearance(models.Model):
    def __str__(self):
        return f'{self.pokemon} in {self.game}'
    base_hp: models.IntegerField = models.IntegerField(default=0)
    base_speed: models.IntegerField = models.IntegerField(default=0)
    base_attack: models.IntegerField = models.IntegerField(default=0)
    base_defence: models.IntegerField = models.IntegerField(default=0)
    base_sp_attack: models.IntegerField = models.IntegerField(default=0)
    base_sp_defence: models.IntegerField = models.IntegerField(default=0)

    pokemon: models.ForeignKey = models.ForeignKey(Pokemon,
                                                   on_delete=models.PROTECT)
    game: models.ForeignKey = models.ForeignKey(Game,
                                                on_delete=models.PROTECT)


class Attack(models.Model):
    def __str__(self):
        return f'{self.name}'
    name: models.TextField = models.TextField(primary_key=True)
    pp: models.IntegerField = models.IntegerField(default=0)
    power: models.IntegerField = models.IntegerField(default=0)
    priority: models.IntegerField = models.IntegerField(default=0)
    accuracy: models.IntegerField = models.IntegerField(default=0)
    tm_number: models.IntegerField = models.IntegerField(default=None,
                                                         blank=True,
                                                         null=True)


class PokemonCanLearn(models.Model):
    def __str__(self):
        return f'{self.appearance}: {self.attack}'
    at_level: models.IntegerField = models.IntegerField(default=0)
    appearance: models.ForeignKey = models.ForeignKey(PokemonAppearance,
                                                      on_delete=models.CASCADE)
    attack: models.ForeignKey = models.ForeignKey(Attack,
                                                  on_delete=models.CASCADE)


class TypeMatchup(models.Model):
    def __str__(self):
        return f'{self.this} vs {self.other}'
    effectiveness_multiplier: models.FloatField = models.FloatField(default=0)
    this: models.ForeignKey = models.ForeignKey(Type,
                                                on_delete=models.CASCADE,
                                                related_name='+')
    other: models.ForeignKey = models.ForeignKey(Type,
                                                 on_delete=models.CASCADE,
                                                 related_name='+')


class AttackTypes(models.Model):
    def __str__(self):
        return f'{self.attack}: {self.attack_type}'
    attack: models.ForeignKey = models.ForeignKey(Attack,
                                                  on_delete=models.CASCADE)
    attack_type: models.ForeignKey = models.ForeignKey(Type,
                                                       on_delete=models.CASCADE)
