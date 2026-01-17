from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select
from datetime import date
from uuid import uuid4
from models import Game
from database import Database

# Create the FastAPI application instance
# This is the main entry point for your API
app = FastAPI()

# Configure CORS (Cross-Origin Resource Sharing)
# This allows your frontend (running on localhost:5173) to make requests
# to your backend API (running on localhost:8000)
#
# Without this, browsers block cross-origin requests for security reasons.
# This is safe for local development, but in production you should
# specify only the domains that should have access to your API.
app.add_middleware(
    CORSMiddleware,
    # allow_origins: List of origins that can access the API
    # ["*"] would allow ALL origins (not recommended for production)
    # For now, we only allow our local frontend
    allow_origins=["http://localhost:5173"],
    # allow_credentials: Allow cookies and authentication headers
    allow_credentials=True,
    # allow_methods: Which HTTP methods are allowed (GET, POST, PUT, DELETE, etc.)
    # ["*"] allows all methods
    allow_methods=["*"],
    # allow_headers: Which HTTP headers can be sent in requests
    # ["*"] allows all headers
    allow_headers=["*"],
)

# Create database instance
# This handles all database connections and sessions
db = Database()

# Constants
OBJECTS_PER_PAGE = 10


# GET /api/games
# Query Params
#  - page <int> required
@app.get("/api/games")
def index(page_number: int = 10):
    # TODO: Uncomment once we are ready to serve live data from the DB.
    # with db.create_session() as session:
    #     statement = select(Game).limit(OBJECTS_PER_PAGE)
    #     results = session.exec(statement)
    #     games = results.all()

    # TODO: Remove mocking once we are retrieving games from the DB.
    games = [
        {
            "id": str(uuid4()),
            "title": "The Legend of Zelda: Breath of the Wild",
            "description": "Step into a world of discovery, exploration, and adventure in this open-air adventure game.",
            "release_date": date(2017, 3, 3),
            "review_score": 97,
            "platforms": {"nintendo_switch": True, "wii_u": True},
            "player_count": 1,
        },
        {
            "id": str(uuid4()),
            "title": "Elden Ring",
            "description": "A vast world where open fields with a variety of situations and huge dungeons await.",
            "release_date": date(2022, 2, 25),
            "review_score": 96,
            "platforms": {"pc": True, "ps5": True, "ps4": True, "xbox_one": True},
            "player_count": 4,
        },
        {
            "id": str(uuid4()),
            "title": "Red Dead Redemption 2",
            "description": "An epic tale of life in America's unforgiving heartland.",
            "release_date": date(2018, 10, 26),
            "review_score": 97,
            "platforms": {"pc": True, "ps4": True, "xbox_one": True},
            "player_count": 32,
        },
        {
            "id": str(uuid4()),
            "title": "God of War Ragnarok",
            "description": "Embark on an epic journey as Kratos and Atreus struggle with holding on and letting go.",
            "release_date": date(2022, 11, 9),
            "review_score": 94,
            "platforms": {"ps5": True, "ps4": True, "pc": True},
            "player_count": 1,
        },
        {
            "id": str(uuid4()),
            "title": "Hades",
            "description": "Defy the god of the dead as you hack and slash out of the Underworld.",
            "release_date": date(2020, 9, 17),
            "review_score": 93,
            "platforms": {
                "pc": True,
                "nintendo_switch": True,
                "ps5": True,
                "xbox_one": True,
            },
            "player_count": 1,
        },
        {
            "id": str(uuid4()),
            "title": "Minecraft",
            "description": "A game about placing blocks and going on adventures.",
            "release_date": date(2011, 11, 18),
            "review_score": 93,
            "platforms": {
                "pc": True,
                "ps4": True,
                "xbox_one": True,
                "nintendo_switch": True,
                "mobile": True,
            },
            "player_count": 8,
        },
        {
            "id": str(uuid4()),
            "title": "Portal 2",
            "description": "A first-person puzzle-platform video game with a Portal gun.",
            "release_date": date(2011, 4, 19),
            "review_score": 95,
            "platforms": {
                "pc": True,
                "ps3": True,
                "xbox_360": True,
                "linux": True,
                "mac": True,
            },
            "player_count": 2,
        },
        {
            "id": str(uuid4()),
            "title": "Hollow Knight",
            "description": "Forge your own path in Hollow Knight! An epic action adventure through a vast ruined kingdom.",
            "release_date": date(2017, 2, 24),
            "review_score": 90,
            "platforms": {
                "pc": True,
                "nintendo_switch": True,
                "ps4": True,
                "xbox_one": True,
            },
            "player_count": 1,
        },
        {
            "id": str(uuid4()),
            "title": "Celeste",
            "description": "Help Madeline survive her inner demons on her journey to the top of Celeste Mountain.",
            "release_date": date(2018, 1, 25),
            "review_score": 91,
            "platforms": {
                "pc": True,
                "nintendo_switch": True,
                "ps4": True,
                "xbox_one": True,
            },
            "player_count": 1,
        },
        {
            "id": str(uuid4()),
            "title": "Stardew Valley",
            "description": "You've inherited your grandfather's old farm plot in Stardew Valley.",
            "release_date": date(2016, 2, 26),
            "review_score": 89,
            "platforms": {
                "pc": True,
                "nintendo_switch": True,
                "ps4": True,
                "xbox_one": True,
                "mobile": True,
            },
            "player_count": 4,
        },
        {
            "id": str(uuid4()),
            "title": "Dark Souls III",
            "description": "As fires fade and the world falls into ruin, journey into a universe filled with colossal enemies.",
            "release_date": date(2016, 4, 12),
            "review_score": 89,
            "platforms": {"pc": True, "ps4": True, "xbox_one": True},
            "player_count": 4,
        },
        {
            "id": str(uuid4()),
            "title": "The Witcher 3: Wild Hunt",
            "description": "You are Geralt of Rivia, mercenary monster slayer.",
            "release_date": date(2015, 5, 19),
            "review_score": 93,
            "platforms": {
                "pc": True,
                "ps4": True,
                "xbox_one": True,
                "nintendo_switch": True,
            },
            "player_count": 1,
        },
        {
            "id": str(uuid4()),
            "title": "Baldur's Gate 3",
            "description": "Gather your party and return to the Forgotten Realms in a tale of fellowship and betrayal.",
            "release_date": date(2023, 8, 3),
            "review_score": 96,
            "platforms": {"pc": True, "ps5": True, "xbox_one_x": True},
            "player_count": 4,
        },
        {
            "id": str(uuid4()),
            "title": "Super Mario Odyssey",
            "description": "Join Mario on a massive, globe-trotting 3D adventure!",
            "release_date": date(2017, 10, 27),
            "review_score": 97,
            "platforms": {"nintendo_switch": True},
            "player_count": 2,
        },
        {
            "id": str(uuid4()),
            "title": "Disco Elysium",
            "description": "A groundbreaking open world role playing game with an insane amount of choice and consequence.",
            "release_date": date(2019, 10, 15),
            "review_score": 91,
            "platforms": {
                "pc": True,
                "ps5": True,
                "ps4": True,
                "nintendo_switch": True,
            },
            "player_count": 1,
        },
    ]

    return {"data": games}
