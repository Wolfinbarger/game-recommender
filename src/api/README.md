# Python Documentation

## Overview
We are using [FastAPI](https://fastapi.tiangolo.com/) to build our API to serve our core Game Recommender application. To serve this API, we are using [Uvicorn](https://www.uvicorn.org/).

## How to run locally
Install required modules:
`pip install --user -r requirements.txt`

Start API server: `uvicorn main:app --reload`

Open `http://127.0.0.1:8000/` in your browser to test.

## Swagger
FastAPI auto generates Swagger docs at the `/docs` endpoint.
`http://127.0.0.1:8000/docs`
