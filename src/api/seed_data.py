"""
Database Seed Script

This script populates the database with sample game data for development and testing.
Run this script to quickly add dummy data to your database.

Usage:
    python seed_data.py

Or from Docker:
    docker compose exec backend python seed_data.py
"""

from database import Database
from models import Game, Platform, Multiplayer
from datetime import date
import random

# Sample game data
SAMPLE_GAMES = [
    {
        "title": "The Legend of Zelda: Breath of the Wild",
        "description": "Step into a world of discovery, exploration, and adventure in this open-air adventure game.",
        "release_date": date(2017, 3, 3),
        "review_score": 97,
        "platforms": {"nintendo_switch": True, "wii_u": True},
        "player_count": 1
    },
    {
        "title": "Elden Ring",
        "description": "A vast world where open fields with a variety of situations and huge dungeons await.",
        "release_date": date(2022, 2, 25),
        "review_score": 96,
        "platforms": {"pc": True, "ps5": True, "ps4": True, "xbox_one": True},
        "player_count": 4
    },
    {
        "title": "Red Dead Redemption 2",
        "description": "An epic tale of life in America's unforgiving heartland.",
        "release_date": date(2018, 10, 26),
        "review_score": 97,
        "platforms": {"pc": True, "ps4": True, "xbox_one": True},
        "player_count": 32
    },
    {
        "title": "God of War Ragnarok",
        "description": "Embark on an epic journey as Kratos and Atreus struggle with holding on and letting go.",
        "release_date": date(2022, 11, 9),
        "review_score": 94,
        "platforms": {"ps5": True, "ps4": True, "pc": True},
        "player_count": 1
    },
    {
        "title": "Hades",
        "description": "Defy the god of the dead as you hack and slash out of the Underworld.",
        "release_date": date(2020, 9, 17),
        "review_score": 93,
        "platforms": {"pc": True, "nintendo_switch": True, "ps5": True, "xbox_one": True},
        "player_count": 1
    },
    {
        "title": "Minecraft",
        "description": "A game about placing blocks and going on adventures.",
        "release_date": date(2011, 11, 18),
        "review_score": 93,
        "platforms": {"pc": True, "ps4": True, "xbox_one": True, "nintendo_switch": True, "mobile": True},
        "player_count": 8
    },
    {
        "title": "Portal 2",
        "description": "A first-person puzzle-platform video game with a Portal gun.",
        "release_date": date(2011, 4, 19),
        "review_score": 95,
        "platforms": {"pc": True, "ps3": True, "xbox_360": True, "linux": True, "mac": True},
        "player_count": 2
    },
    {
        "title": "Hollow Knight",
        "description": "Forge your own path in Hollow Knight! An epic action adventure through a vast ruined kingdom.",
        "release_date": date(2017, 2, 24),
        "review_score": 90,
        "platforms": {"pc": True, "nintendo_switch": True, "ps4": True, "xbox_one": True},
        "player_count": 1
    },
    {
        "title": "Celeste",
        "description": "Help Madeline survive her inner demons on her journey to the top of Celeste Mountain.",
        "release_date": date(2018, 1, 25),
        "review_score": 91,
        "platforms": {"pc": True, "nintendo_switch": True, "ps4": True, "xbox_one": True},
        "player_count": 1
    },
    {
        "title": "Stardew Valley",
        "description": "You've inherited your grandfather's old farm plot in Stardew Valley.",
        "release_date": date(2016, 2, 26),
        "review_score": 89,
        "platforms": {"pc": True, "nintendo_switch": True, "ps4": True, "xbox_one": True, "mobile": True},
        "player_count": 4
    },
    {
        "title": "Dark Souls III",
        "description": "As fires fade and the world falls into ruin, journey into a universe filled with colossal enemies.",
        "release_date": date(2016, 4, 12),
        "review_score": 89,
        "platforms": {"pc": True, "ps4": True, "xbox_one": True},
        "player_count": 4
    },
    {
        "title": "The Witcher 3: Wild Hunt",
        "description": "You are Geralt of Rivia, mercenary monster slayer.",
        "release_date": date(2015, 5, 19),
        "review_score": 93,
        "platforms": {"pc": True, "ps4": True, "xbox_one": True, "nintendo_switch": True},
        "player_count": 1
    },
    {
        "title": "Baldur's Gate 3",
        "description": "Gather your party and return to the Forgotten Realms in a tale of fellowship and betrayal.",
        "release_date": date(2023, 8, 3),
        "review_score": 96,
        "platforms": {"pc": True, "ps5": True, "xbox_one_x": True},
        "player_count": 4
    },
    {
        "title": "Super Mario Odyssey",
        "description": "Join Mario on a massive, globe-trotting 3D adventure!",
        "release_date": date(2017, 10, 27),
        "review_score": 97,
        "platforms": {"nintendo_switch": True},
        "player_count": 2
    },
    {
        "title": "Disco Elysium",
        "description": "A groundbreaking open world role playing game with an insane amount of choice and consequence.",
        "release_date": date(2019, 10, 15),
        "review_score": 91,
        "platforms": {"pc": True, "ps5": True, "ps4": True, "nintendo_switch": True},
        "player_count": 1
    },
]


def seed_database():
    """
    Seeds the database with sample game data.

    This function creates Platform, Multiplayer, and Game records
    for each game in the SAMPLE_GAMES list.
    """
    db = Database()

    with db.create_session() as session:
        # Check if data already exists
        existing_games = session.query(Game).count()
        if existing_games > 0:
            print(f"Database already has {existing_games} games. Skipping seed.")
            print("To reseed, clear the database first.")
            return

        print("Seeding database with sample games...")

        for game_data in SAMPLE_GAMES:
            # Create Platform record
            platform = Platform(**game_data["platforms"])
            session.add(platform)
            session.flush()  # Get the platform ID

            # Create Multiplayer record
            multiplayer = Multiplayer(player_count=game_data["player_count"])
            session.add(multiplayer)
            session.flush()  # Get the multiplayer ID

            # Create Game record
            game = Game(
                title=game_data["title"],
                description=game_data["description"],
                release_date=game_data["release_date"],
                review_score=game_data["review_score"],
                platform_id=platform.id,
                multiplayer_id=multiplayer.id
            )
            session.add(game)
            print(f"  Added: {game_data['title']}")

        session.commit()
        print(f"\nSuccessfully seeded {len(SAMPLE_GAMES)} games!")


def clear_database():
    """
    Clears all game data from the database.
    Use with caution!
    """
    db = Database()

    with db.create_session() as session:
        # Delete in order to respect foreign key constraints
        games_deleted = session.query(Game).delete()
        multiplayer_deleted = session.query(Multiplayer).delete()
        platforms_deleted = session.query(Platform).delete()
        session.commit()

        print(f"Cleared database:")
        print(f"  - {games_deleted} games deleted")
        print(f"  - {multiplayer_deleted} multiplayer records deleted")
        print(f"  - {platforms_deleted} platform records deleted")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--clear":
        clear_database()
    else:
        seed_database()
