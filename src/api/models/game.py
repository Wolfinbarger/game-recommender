# import platforms
# import multiplayer
from src.api.models import platforms, multiplayer

class Game:
    """
    Args:
        title (str): Title of game.
        description (str, optional): Description of game.
        available_platforms (Platform, optional): Platform object that identifies which platforms the game is available on.
    """

    def __init__(self, title, description=None, available_platforms=None, release_date=None, available_multiplayer=None):
        self._title = title
        self._description = description
        self._release_date = release_date

        if available_platforms is None:
            self._available_platforms = platforms.Platforms()
        else:
            self._available_platforms = available_platforms

        if available_multiplayer is None:
            self._available_multiplayer = multiplayer.Multiplayer()
        else:
            self._available_multiplayer = available_multiplayer

    @property
    def title(self):
        return self._title.title()

    @property
    def description(self):
        return self._description

    @property
    def release_date(self):
        return self._release_date

    @property
    def available_platforms(self):
        return self._available_platforms.to_json()

    @property
    def available_multiplayer(self):
        return self._available_multiplayer.to_json()

    @title.setter
    def title(self, value):
        self._title = value

    @description.setter
    def description(self, value):
        self._description = value

    @release_date.setter
    def release_date(self, value):
        self._release_date = value

    @available_platforms.setter
    def available_platforms(self, value):
        self._available_platforms = value

    @available_multiplayer.setter
    def available_multiplayer(self, value):
        self._available_multiplayer = value

    def to_json(self):
        return {
            "title": self.title,
            "description": self.description,
            "release_date": self.release_date,
            "platforms": self.available_platforms,
            "multiplayer": self.available_multiplayer
        }