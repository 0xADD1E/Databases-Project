# Generated by Django 2.2.1 on 2019-05-04 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_enable-getorcreate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonAbilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Pokemon')),
                ('pokemon_ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Abilities')),
            ],
        ),
    ]