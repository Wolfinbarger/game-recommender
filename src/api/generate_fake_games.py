#
# Description: Uses the Faker library to create fake records in the database for the Game,
# Multiplayer, and Platform models.
#
from faker import Faker
import random
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'

# Set up the Django environment
django.setup()

from games.models import Game, Platform, Multiplayer

NUM_OF_GAMES_TO_CREATE = 100

fake = Faker()
data = []
for i in range(NUM_OF_GAMES_TO_CREATE):
    title = ' '.join(fake.words(nb=random.randint(1, 3)))
    description = fake.paragraph()
    release_date = fake.date()

    platform = Platform()
    platform.save()

    multiplayer = Multiplayer(
        player_count=random.randint(1, 20)
    )
    multiplayer.save()

    game = Game(
        title=title,
        description=description,
        platform=platform,
        release_date=release_date,
        multiplayer=multiplayer
    )
    game.save()
