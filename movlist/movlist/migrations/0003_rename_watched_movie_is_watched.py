# Generated by Django 3.2.9 on 2021-12-05 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movlist', '0002_movie_watched'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='watched',
            new_name='is_watched',
        ),
    ]
