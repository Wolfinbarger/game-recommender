from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select

from .models import Game
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from os import environ

load_dotenv("../../.env")

# DOCKER_ENABLED is set in the Dockerfile
if 'DOCKER_ENABLED' in environ:
    DB_HOST = "host.docker.internal"
else:
    DB_HOST = "localhost"

# PASSWORD is optional for setting up Postgresql DB
if "PASSWORD" not in environ:
    environ["PASSWORD"] = ""

app = FastAPI()
# gdb = import_module("services.igdb")

# Create PostgresSQL Database connection using SQLModel
DB_NAME = "game-recommender"
USER = environ["USER"]
PASSWORD = environ["PASSWORD"]

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{DB_HOST}/{DB_NAME}"
print(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# Constants
OBJECTS_PER_PAGE = 10

# GET /api/games
# Query Params
#  - page <int> required
@app.get("/api/games")
def index(page_number: int):
    #game_list = Game.objects.all().order_by("title")

    # Grab game objects based on page number using sqlalchemy
    #page = Game.query.paginate(page=page_number, per_page=OBJECTS_PER_PAGE).items

    with Session(engine) as session:
        statement = select(Game).limit(OBJECTS_PER_PAGE)
        results = session.exec(statement)
        games = results.all()
        print(games)
    #data = [game.to_json() for game in page]

    # Enrich game data from database with IGDB data
    # igdb_api = igdb.IGDB()
    # for game in data:
    #     igdb_search_results = igdb_api.search(game.title)
    #     print(igdb_search_results[0].get('id'))

    return {"data": games}