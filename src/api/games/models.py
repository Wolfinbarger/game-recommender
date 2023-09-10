from django.db import models


class Platform(models.Model):
    pc = models.BooleanField(default=False, db_column='platform_pc')
    ps4 = models.BooleanField(default=False, db_column='platform_ps4')
    ps5 = models.BooleanField(default=False, db_column='platform_ps5')
    xbox_one_x = models.BooleanField(default=False, db_column='platform_xbox_one_x')
    nintendo_switch = models.BooleanField(default=False, db_column='platform_nintendo_switch')

    def __str__(self):
        return self.to_json().__str__()

    def to_json(self):
        return {
            "pc": self.pc,
            "ps4": self.ps4,
            "ps5": self.ps5,
            "xbox_one_x": self.xbox_one_x,
            "nintendo_switch": self.nintendo_switch
        }


class Multiplayer(models.Model):
    player_count = models.IntegerField(db_column='multiplayer_player_count')

    def __str__(self):
        return self.to_json().__str__()

    def to_json(self):
        return {
            "player_count": self.player_count
        }


class Game(models.Model):
    title = models.CharField(max_length=50, db_column='game_title')
    description = models.TextField(db_column='game_description')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, db_column='game_platform')
    release_date = models.DateField(db_column='game_release_date')
    multiplayer = models.ForeignKey(Multiplayer, on_delete=models.CASCADE, db_column='game_multiplayer')

    def __str__(self):
        return self.to_json().__str__()

    def to_json(self):
        return {
            "title": self.title,
            "description": self.description,
            "platform": self.platform.to_json(),
            "release_date": self.release_date.__str__(),
            "multiplayer": self.multiplayer.to_json()
        }


