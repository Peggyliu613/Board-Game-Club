# Generated by Django 2.2.7 on 2019-12-19 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_game_club_app', '0004_auto_20191219_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characters',
            name='isusing',
            field=models.BooleanField(default=False),
        ),
    ]