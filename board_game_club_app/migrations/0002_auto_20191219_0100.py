# Generated by Django 2.2.7 on 2019-12-19 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_game_club_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='time',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateField(),
        ),
    ]
