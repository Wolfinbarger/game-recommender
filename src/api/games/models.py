from django.db import models
from django.contrib.postgres.fields import ArrayField


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


class IGDBGame(models.Model):
    # The IGDB id of the game
    id = models.IntegerField(primary_key=True, db_column='igdb_game_id')
    # The aggregated rating of the game
    aggregated_rating = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_aggregated_rating'), blank=True, null=True)
    # The amount of ratings the game has received
    aggregated_rating_count = models.IntegerField(null=True, blank=True, db_column='igdb_game_aggregated_rating_count')
    # The alternative names of the game
    alternative_names = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_alternative_names'), blank=True, null=True)
    # The artworks associated with the game
    artworks = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_artworks'), blank=True, null=True)
    # The bundles that include the game
    bundles = ArrayField(models.IntegerField( null=True, blank=True, db_column='igdb_game_bundles'), blank=True, null=True)
    # The category of the game
    category = models.IntegerField(null=True, blank=True, db_column='igdb_game_category')
    # The checksum of the game
    checksum = models.UUIDField(null=True, blank=True, db_column='igdb_game_checksum')
    # The collection that the game belongs to
    collection = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_collection'), blank=True, null=True)
    # The cover image of the game
    cover = models.IntegerField(null=True, blank=True, db_column='igdb_game_cover')
    # The creation date of the game
    created_at = models.IntegerField(null=True, blank=True, db_column='igdb_game_created_at')
    # The DLCs and expansions of the game
    dlcs = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_dlcs'), blank=True, null=True)
    # The external games linked to the game
    external_games = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_external_games'), blank=True, null=True)
    # The first release date of the game
    first_release_date = models.IntegerField(null=True, blank=True, db_column='igdb_game_first_release_date')
    # The follows count of the game
    follows = models.IntegerField(null=True, blank=True, db_column='igdb_game_follows')
    # The franchises that the game belongs to
    franchises = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_franchises'), blank=True, null=True)
    # The game engines used by the game
    game_engines = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_game_engines'), blank=True, null=True)
    # The game modes available in the game
    game_modes = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_game_modes'), blank=True, null=True)
    # The genres of the game
    genres = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_genres'), blank=True, null=True)
    # The Hypescore of the game
    hypes = models.IntegerField(null=True, blank=True, db_column='igdb_game_hypes')
    # The involved companies in the game
    involved_companies = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_involved_companies'), blank=True, null=True)
    # The keywords associated with the game
    keywords = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_keywords'), blank=True, null=True)
    # The multiplayer modes available in the game
    multiplayer_modes = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_multiplayer_modes'), blank=True, null=True)
    # The name of the game
    name = models.CharField(max_length=255, null=True, blank=True, db_column='igdb_game_name')
    # The parent game of the game
    parent_game = models.IntegerField(null=True, blank=True, db_column='igdb_game_parent_game')
    # The platforms that the game is released on
    platforms = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_platforms'), blank=True, null=True)
    # The player perspectives of the game
    player_perspectives = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_player_perspectives'), blank=True, null=True)
    # The rating of the game
    rating = models.FloatField(null=True, blank=True, db_column='igdb_game_rating')
    # The amount of ratings the game has received
    rating_count = models.IntegerField(null=True, blank=True, db_column='igdb_game_rating_count')
    # The release dates of the game
    release_dates = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_release_dates'), blank=True, null=True)
    # The screenshots of the game
    screenshots = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_screenshots'), blank=True, null=True)
    # The similar games to the game
    similar_games = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_similar_games'), blank=True, null=True)
    # The slug of the game
    slug = models.SlugField(max_length=255, null=True, blank=True, db_column='igdb_game_slug')
    # The standalone expansions of the game
    standalone_expansions = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_standalone_expansions'), blank=True, null=True)
    # The status of the game
    status = models.IntegerField(null=True, blank=True, db_column='igdb_game_status')
    # The storylines of the game
    storylines = models.TextField(null=True, blank=True, db_column='igdb_game_storylines')
    # The summary of the game
    summary = models.TextField(null=True, blank=True, db_column='igdb_game_summary')
    # The tags of the game
    tags = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_tags'), blank=True, null=True)
    # The themes of the game
    themes = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_themes'), blank=True, null=True)
    # The total rating of the game
    total_rating = models.FloatField(null=True, blank=True, db_column='igdb_game_total_rating')
    # The amount of total ratings the game has received
    total_rating_count = models.IntegerField(null=True, blank=True, db_column='igdb_game_total_rating_count')
    # The update date of the game
    updated_at = models.IntegerField(null=True, blank=True, db_column='igdb_game_updated_at')
    # The URL of the game
    url = models.URLField(max_length=255, null=True, blank=True, db_column='igdb_game_url')
    # The version parent of the game
    version_parent = models.IntegerField(null=True, blank=True, db_column='igdb_game_version_parent')
    # The version title of the game
    version_title = models.CharField(max_length=255, null=True, blank=True, db_column='igdb_game_version_title')
    # The videos associated with the game
    videos = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_videos'), blank=True, null=True)
    # The websites of the game
    websites = ArrayField(models.IntegerField(null=True, blank=True, db_column='igdb_game_websites'), blank=True, null=True)

    def __str__(self):
        return self.to_json().__str__()

    def to_json(self):
        return to_json(self.__dict__.items())