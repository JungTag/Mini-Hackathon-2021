# Generated by Django 3.2.5 on 2021-07-21 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_rating_rut'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='total_cnt',
            field=models.IntegerField(default=0),
        ),
    ]