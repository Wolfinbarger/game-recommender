from django.db import models


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


class Platform(models.Model):
    # Desktop
    pc = models.BooleanField(default=False, db_column='platform_pc')
    linux = models.BooleanField(default=False, db_column='platform_linux')
    mac = models.BooleanField(default=False, db_column='platform_mac')
    web_browser = models.BooleanField(default=False, db_column='platform_web_browser')

    # Playstation
    psp = models.BooleanField(default=False, db_column='platform_psp')
    vita = models.BooleanField(default=False, db_column='platform_vita')
    ps1 = models.BooleanField(default=False, db_column='platform_ps1')
    ps2 = models.BooleanField(default=False, db_column='platform_ps2')
    ps3 = models.BooleanField(default=False, db_column='platform_ps3')
    ps4 = models.BooleanField(default=False, db_column='platform_ps4')
    ps5 = models.BooleanField(default=False, db_column='platform_ps5')

    # Xbox
    xbox = models.BooleanField(default=False, db_column='platform_xbox')
    xbox_360 = models.BooleanField(default=False, db_column='platform_xbox_360')
    xbox_one = models.BooleanField(default=False, db_column='platform_xbox_one')
    xbox_one_x = models.BooleanField(default=False, db_column='platform_xbox_one_x')

    # Nintendo
    nes = models.BooleanField(default=False, db_column='platform_nes')
    super_nintendo = models.BooleanField(default=False, db_column='platform_super_nintendo')
    n64 = models.BooleanField(default=False, db_column='platform_64')
    game_boy = models.BooleanField(default=False, db_column='platform_game_boy')
    game_boy_color = models.BooleanField(default=False, db_column='platform_game_boy_color')
    game_boy_advance = models.BooleanField(default=False, db_column='platform_game_boy_advance')
    gamecube = models.BooleanField(default=False, db_column='platform_gamecube')
    wii = models.BooleanField(default=False, db_column='platform_wii')
    wii_u = models.BooleanField(default=False, db_column='platform_wii_u')
    nintendo_switch = models.BooleanField(default=False, db_column='platform_nintendo_switch')
    nintendo_ds = models.BooleanField(default=False, db_column='platform_nintendo_ds')
    nintendo_3ds = models.BooleanField(default=False, db_column='platform_3ds')

    # Mobile
    mobile = models.BooleanField(default=False, db_column='platform_mobile')
    ios = models.BooleanField(default=False, db_column='platform_ios')
    android = models.BooleanField(default=False, db_column='platform_android')
    windows_mobile = models.BooleanField(default=False, db_column='platform_windows_mobile')

    # Retro
    # TurboGrafx-16 - https://en.wikipedia.org/wiki/TurboGrafx-16
    tg16 = models.BooleanField(default=False, db_column='platform_tg16')
    # TurboGrafx-CD - https://www.giantbomb.com/turbografx-cd/3045-53/
    tcd = models.BooleanField(default=False, db_column='platform_tcd')
    # N Gage - https://en.wikipedia.org/wiki/N-Gage_(device)
    n_gage = models.BooleanField(default=False, db_column='platform_n_gage')
    arcade = models.BooleanField(default=False, db_column='platform_arcade')
    sega_saturn = models.BooleanField(default=False, db_column='platform_sega_saturn')
    sega_genesis = models.BooleanField(default=False, db_column='platform_sega_genesis')
    dreamcast = models.BooleanField(default=False, db_column='platform_dreamcast')
    blackberry = models.BooleanField(default=False, db_column='platform_blackberry')
    neo_geo = models.BooleanField(default=False, db_column='platform_neo_geo')
    neo_geo_pocket_color = models.BooleanField(default=False, db_column='platform_neo_geo_pocket_color')
    neo_geo_pocket = models.BooleanField(default=False, db_column='platform_neo_geo_pocket')
    # Famicom Disk System - https://en.wikipedia.org/wiki/Famicom_Disk_System
    famicom = models.BooleanField(default=False, db_column='platform_famicom')
    # Zeebo - https://en.wikipedia.org/wiki/Zeebo
    zeebo = models.BooleanField(default=False, db_column='platform_zeebo')

    # Other
    web_os = models.BooleanField(default=False, db_column='platform_web_os')

    def __str__(self):
        return self.to_json().__str__()

    def to_json(self):
        return to_json(self.__dict__.items())


class Multiplayer(models.Model):
    player_count = models.IntegerField(null=True, db_column='multiplayer_player_count')

    def __str__(self):
        return self.to_json().__str__()

    def to_json(self):
        return to_json(self.__dict__.items())


class Game(models.Model):
    # Mandatory Field
    title = models.CharField(db_column='game_title')

    # Nullable Fields
    description = models.TextField(null=True, db_column='game_description')
    release_date = models.DateField(null=True, db_column='game_release_date')
    review_score = models.IntegerField(null=True, db_column='game_review_score')

    # Foreign Keys
    multiplayer = models.ForeignKey(Multiplayer, on_delete=models.CASCADE, db_column='game_multiplayer')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, db_column='game_platform')

    def __str__(self):
        return self.to_json().__str__()

    def to_json(self):
        return to_json(self.__dict__.items())
