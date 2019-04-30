# Generated by Django 2.2 on 2019-04-27 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Pokemon')),
                ('pokemon_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Type')),
            ],
        ),
    ]