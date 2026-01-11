from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import select

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