# Generated by Django 2.2.7 on 2019-12-19 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_game_club_app', '0008_testplayer'),
    ]

    operations = [
        migrations.AddField(
            model_name='testplayer',
            name='order_number',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
