# Generated by Django 2.2 on 2019-05-07 20:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('name', models.TextField(max_length=64, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('name', models.TextField(max_length=64, primary_key=True, serialize=False)),
                ('pp', models.IntegerField(default=0)),
                ('power', models.IntegerField(default=0)),
                ('priority', models.IntegerField(default=0)),
                ('accuracy', models.IntegerField(default=0)),
                ('tm_number', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MIMEType',
            fields=[
                ('mime_string', models.TextField(max_length=64, primary_key=True, serialize=False)),
                ('friendly_name', models.TextField(max_length=128)),
                ('extension', models.TextField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('name', models.TextField(max_length=32, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('pokedex_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(default='', max_length=128)),
                ('weight', models.FloatField(default=0)),
                ('height', models.FloatField(default=0)),
                ('gender_distribution', models.IntegerField(default=0)),
                ('legendary', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonAppearance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_hp', models.IntegerField(default=0)),
                ('base_speed', models.IntegerField(default=0)),
                ('base_attack', models.IntegerField(default=0)),
                ('base_defence', models.IntegerField(default=0)),
                ('base_sp_attack', models.IntegerField(default=0)),
                ('base_sp_defence', models.IntegerField(default=0)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='frontend.Pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('name', models.TextField(max_length=32, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeMatchup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effectiveness_multiplier', models.FloatField(default=0)),
                ('other', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='frontend.Type')),
                ('this', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='frontend.Type')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Pokemon')),
                ('pokemon_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Type')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEvolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evolves_to', to='frontend.Pokemon')),
                ('evolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evolved_from', to='frontend.Pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonCanLearn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('at_level', models.IntegerField(default=0)),
                ('appearance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.PokemonAppearance')),
                ('attack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Attack')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonAbility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Pokemon')),
                ('pokemon_ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Ability')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.TextField(max_length=128)),
                ('data', models.BinaryField(default=b'')),
                ('mime', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='frontend.MIMEType')),
                ('of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('name', models.TextField(max_length=32, primary_key=True, serialize=False)),
                ('release_date', models.DateField(default=datetime.datetime.now)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='frontend.Platform')),
            ],
        ),
        migrations.CreateModel(
            name='AttackTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Attack')),
                ('attack_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Type')),
            ],
        ),
    ]
