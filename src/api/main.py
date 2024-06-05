from fastapi import FastAPI
from sqlmodel import select

from .models import Game
from .database import Database

app = FastAPI()
db = Database()

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

    with db.create_session() as session:
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