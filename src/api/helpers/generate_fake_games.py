#
# Description: Uses the Faker library to generate a JSON file with fake game data using the Game and Platform models.
#
from faker import Faker
import random
import json

from src.api.models import platforms, multiplayer, game

NUM_OF_GAMES_TO_CREATE = 100

fake = Faker()
data = []
for i in range(NUM_OF_GAMES_TO_CREATE):
    title = ' '.join(fake.words(nb=random.randint(1, 3)))
    description = fake.paragraph()
    release_date = str(fake.date())
    available_platforms = platforms.Platforms()
    available_multiplayer = multiplayer.Multiplayer(random.randint(1, 20))
    g = game.Game(title, description, available_platforms, release_date, available_multiplayer)

    data.append(g.to_json())

with open('../../../data/fake_games_dataset.json', 'w+') as outfile:
    json.dump(data, outfile, indent=1)
