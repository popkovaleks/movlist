# Generated by Django 3.2.9 on 2021-12-05 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='watched',
            field=models.BooleanField(default=False),
        ),
    ]
