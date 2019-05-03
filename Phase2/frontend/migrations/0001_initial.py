# Generated by Django 2.2 on 2019-04-25 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('pp', models.IntegerField()),
                ('power', models.IntegerField()),
                ('priority', models.IntegerField()),
                ('accuracy', models.IntegerField()),
                ('tm_number', models.IntegerField(
                    blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MIMEType',
            fields=[
                ('mime_string', models.TextField(
                    primary_key=True, serialize=False)),
                ('friendly_name', models.TextField()),
                ('extension', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('pokedex_id', models.IntegerField(
                    primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('gender_distribution', models.IntegerField()),
                ('legendary', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PokemonAppearance',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('base_hp', models.IntegerField()),
                ('base_speed', models.IntegerField()),
                ('base_attack', models.IntegerField()),
                ('base_defence', models.IntegerField()),
                ('base_sp_attack', models.IntegerField()),
                ('base_sp_defence', models.IntegerField()),
                ('game', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='frontend.Game')),
                ('pokemon', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='frontend.Pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeMatchup',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('effectiveness_multiplier', models.FloatField()),
                ('other', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='+', to='frontend.Type')),
                ('this', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name='+', to='frontend.Type')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEvolution',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='evolves_to', to='frontend.Pokemon')),
                ('evolution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                                related_name='evolved_from', to='frontend.Pokemon')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonCanLearn',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('at_level', models.IntegerField()),
                ('appearance', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='frontend.PokemonAppearance')),
                ('attack', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='frontend.Attack')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.TextField()),
                ('data', models.BinaryField()),
                ('mime', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='frontend.MIMEType')),
                ('of', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='frontend.Pokemon')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to='frontend.Platform'),
        ),
        migrations.CreateModel(
            name='AttackTypes',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('attack', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='frontend.Attack')),
                ('attack_type', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='frontend.Type')),
            ],
        ),
    ]
