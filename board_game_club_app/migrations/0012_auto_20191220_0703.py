# Generated by Django 2.2.7 on 2019-12-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board_game_club_app', '0011_auto_20191220_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avalon_characters',
            name='function',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
