# Generated by Django 2.2 on 2019-05-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_auto_20190501_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.FloatField(),
        ),
    ]
