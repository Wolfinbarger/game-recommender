from typing import Union

from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
def read_root():
    return "Greetings from the Game Recommender application!"


@app.get("/api/games")
def get_all_games():
    # TODO: Switch to using real data when it's available.
    with open('../../data/fake_games_dataset.json', 'r') as data:
        decoder = json.JSONDecoder()
        return decoder.decode(data.read())
