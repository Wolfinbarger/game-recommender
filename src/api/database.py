from sqlmodel import create_engine, Session
from sqlalchemy.orm import sessionmaker
from os import environ
from dotenv import load_dotenv

load_dotenv("../../.env")

class Database:
    def __init__(self):
        # DOCKER_ENABLED is set in the Dockerfile
        if 'DOCKER_ENABLED' in environ:
            self.host = "host.docker.internal"
        else:
            self.host = "localhost"

        # PASSWORD is optional for setting up Postgresql DB
        if "PASSWORD" not in environ:
            environ["PASSWORD"] = ""

        self.name = "game-recommender"
        self.user = environ["USER"]
        self.password = environ["PASSWORD"]

        self.db_url: str = self.create_database_url()

    def create_session(self):
        engine = create_engine(self.db_url)
        #session_local = sessionmaker(autocommit = False, autoflush = False, bind = engine)
        return Session(engine)

    def create_database_url(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}/{self.name}"