from sqlalchemy import Column
from sqlmodel import SQLModel, Field, Relationship, JSON
from typing import Optional, Dict
from datetime import date
from typing import List


def to_json(items):
    data = {}
    for name, value in items:
        # Skip the private attributes that start with '_'
        if name.startswith('_'):
            continue

        if name == "multiplayer_id":
            name = name.replace("_id", "")
            data[name] = Multiplayer.objects.get(id=value).to_json()
        elif name == "platform_id":
            name = name.replace("_id", "")
            data[name] = Platform.objects.get(id=value).to_json()
        else:
            data[name] = value

    return data


class Game(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)

    title: str = Field(alias = 'game_title')

    description: Optional[str] = Field(default = None, alias = 'game_description')
    release_date: Optional[date] = Field(default = None, alias = 'game_release_date')
    review_score: Optional[int] = Field(default = None, alias = 'game_review_score')

    multiplayer_id: Optional[int] = Field(default = None, foreign_key = "multiplayer.id",
                                          alias = 'game_multiplayer')

    # NOTE: A relationship field is used to interact with the related object directly. The back_populates argument
    # specifies the attribute in the related model that should be updated when this model changes.
    multiplayer: Optional["Multiplayer"] = Relationship(back_populates = "games")

    platform_id: Optional[int] = Field(default = None, foreign_key = "platform.id", alias = 'game_platform')
    platform: Optional["Platform"] = Relationship(back_populates = "games")

    def __str__(self):
        return self.to_json().__str__()

    def to_json(self):
        return to_json(self.__dict__.items())


class Platform(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    games: List[Game] = Relationship(back_populates = "platform")

    # Desktop
    pc: bool = Field(default = False)
    linux: bool = Field(default = False)
    mac: bool = Field(default = False)
    web_browser: bool = Field(default = False)

    # Playstation
    psp: bool = Field(default = False)
    vital: bool = Field(default = False)
    ps1: bool = Field(default = False)
    ps2: bool = Field(default = False)
    ps3: bool = Field(default = False)
    ps4: bool = Field(default = False)
    ps5: bool = Field(default = False)

    # Xbox
    xbox: bool = Field(default = False)
    xbox_360: bool = Field(default = False)
    xbox_one: bool = Field(default = False)
    xbox_one_x: bool = Field(default = False)

    # Nintendo
    nes: bool = Field(default = False)
    super_nintendo: bool = Field(default = False)
    n64: bool = Field(default = False)
    game_boy: bool = Field(default = False)
    game_boy_color: bool = Field(default = False)
    game_boy_advance: bool = Field(default = False)
    gamecube: bool = Field(default = False)
    wii: bool = Field(default = False)
    wii_u: bool = Field(default = False)
    nintendo_switch: bool = Field(default = False)
    nintendo_ds: bool = Field(default = False)
    nintendo_3ds: bool = Field(default = False)

    # Mobile
    mobile: bool = Field(default = False)
    ios: bool = Field(default = False)
    android: bool = Field(default = False)
    windows_mobile: bool = Field(default = False)

    # Retro
    # TurboGrafx-16 - https://en.wikipedia.org/wiki/TurboGrafx-16
    tg16: bool = Field(default = False)
    # TurboGrafx-CD - https://www.giantbomb.com/turbografx-cd/3045-53/
    tcd: bool = Field(default = False)
    # N Gage - https://en.wikipedia.org/wiki/N-Gage_(device)
    n_gage: bool = Field(default = False)
    arcade: bool = Field(default = False)
    sega_saturn: bool = Field(default = False)
    sega_genesis: bool = Field(default = False)
    dreamcast: bool = Field(default = False)
    blackberry: bool = Field(default = False)
    neo_geo: bool = Field(default = False)
    neo_geo_pocket_color: bool = Field(default = False)
    neo_geo_pocket: bool = Field(default = False)
    # Famicom Disk System - https://en.wikipedia.org/wiki/Famicom_Disk_System
    famicom: bool = Field(default = False)
    # Zeebo - https://en.wikipedia.org/wiki/Zeebo
    zeebo: bool = Field(default = False)

    # Other
    web_os: bool = Field(default = False)

    def to_json(self):
        return to_json(self.__dict__.items())

    def __str__(self):
        return self.to_json().__str__()


class Multiplayer(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    player_count: Optional[int] = Field(default = None)
    games: List[Game] = Relationship(back_populates = "multiplayer")

    def __str__(self):
        return self.to_json().__str__()

    def to_json(self):
        return to_json(self.__dict__.items())


class IGDBGame(SQLModel, table=True):
    id: Optional[int] = Field(default = None, primary_key = True)
    attrs: Dict = Field(default_factory=dict, sa_column=Column(JSON))

    def __str__(self):
        return self.to_json().__str__()

    def to_json(self):
        return to_json(self.__dict__.items())