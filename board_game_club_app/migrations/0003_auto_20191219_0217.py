# Generated by Django 2.2.7 on 2019-12-19 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_game_club_app', '0002_auto_20191219_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='characters',
            name='isusing',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='time',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
