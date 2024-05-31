#
# Description: Parses and creates new records from our datasets.
#
import os
import django
from dotenv import load_dotenv
import pandas as pd

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'
load_dotenv("../../.env")

# Set up the Django environment
django.setup()
from games.models import Game, Platform, Multiplayer


def parse_platforms(platforms):
    platforms = platforms.replace(",", "").split()
    fields = {}
    for platform in platforms:
        fields[platform_dict[platform]] = True

    return fields


def parse_gamespot_dataset():
    """ Information about Gamespot Dataset

    Platforms
    ['PC', 'NS', 'XONE', 'PS4', 'IOS', 'WIIU', 'LNX', 'MAC', 'AND', '3DS', 'PS3', 'TG16', 'VITA', 'X360', 'SNES',
     'XBOX', 'PS2', 'WII', 'N64', 'NGE', 'PSP', 'MOBI', 'ARC', 'GBC', 'WEB', 'SAT', 'GBA', 'DS', 'DC', 'BB', 'WOS',
     'WINM', 'PS', 'NES', 'GEN', 'NEO', 'TCD', 'FDS', 'GC', 'NGPC', 'ZOD', 'GB', 'NGP']

    Reviews
    ['Early Access', 'Good', 'Great', 'Superb', 'Fair', 'Terrible', 'Mediocre', 'Bad', 'Poor', 'Essential', 'Abysmal']

    Scores
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    gamespot_data = pd.read_csv("../../data/gamespot_dataset.csv")

    for platforms, title, review, score in gamespot_data.values:
        fields = parse_platforms(platforms)
        platform = Platform(**fields)
        platform.save()

        multiplayer = Multiplayer()
        multiplayer.save()

        remove_review_index = title.find(" Review")
        title = title[0:remove_review_index]

        game = Game(
            title=title,
            platform=platform,
            multiplayer=multiplayer,
            review_score=score
        )
        game.save()


def main():
    parse_gamespot_dataset()


platform_dict = {
    "PC": "pc",
    "LNX": "linux",
    "MAC": "mac",
    "WEB": "web_browser",
    "PSP": "psp",
    "VITA": "vita",
    "PS": "ps1",
    "PS2": "ps2",
    "PS3": "ps3",
    "PS4": "ps4",
    "PS5": "ps5",
    "XBOX": "xbox",
    "X360": "xbox_360",
    "XONE": "xbox_one",
    "XONEX": "xbox_one_x",
    "NES": "nes",
    "SNES": "super_nintendo",
    "N64": "n64",
    "GB": "game_boy",
    "GBC": "game_boy_color",
    "GBA": "game_boy_advance",
    "GC": "gamecube",
    "WII": "wii",
    "WIIU": "wii_u",
    "NS": "nintendo_switch",
    "DS": "nintendo_ds",
    "3DS": "nintendo_3ds",
    "MOBI": "mobile",
    "IOS": "ios",
    "AND": "android",
    "WINM": "windows_mobile",
    "TG16": "tg16",
    "TCD": "tcd",
    "NGE": "n_gage",
    "ARC": "arcade",
    "SAT": "sega_saturn",
    "GEN": "sega_genesis",
    "DC": "dreamcast",
    "BB": "blackberry",
    "NEO": "neo_geo",
    "NGPC": "neo_geo_pocket_color",
    "NGP": "neo_geo_pocket",
    "FDS": "famicom",
    "ZOD": "zeebo",
    "WOS": "web_os"
}

if __name__ == "__main__":
    main()