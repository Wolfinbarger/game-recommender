# Generated by Django 4.2.4 on 2023-09-14 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_alter_multiplayer_player_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(db_column='game_title'),
        ),
    ]