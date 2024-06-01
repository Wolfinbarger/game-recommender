#
# Description: Parses and creates new records from our datasets.
#
import os
from dotenv import load_dotenv
import pandas as pd
from models import Game, Platform
from database import Database

load_dotenv("../../.env")

db = Database()

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

    with db.create_session() as session:
        for platforms, title, review, score in gamespot_data.values:
            fields = parse_platforms(platforms)
            # Create Platform object from fields using sqlmodel
            platform = Platform(**fields)
            session.add(platform)

            game = Game(
                title = title,
                platform = platform,
                review_score = score
            )
            session.add(game)

        session.commit()


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