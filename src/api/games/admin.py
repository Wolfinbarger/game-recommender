from django.contrib import admin

from .models import Game, Platform, Multiplayer

admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Multiplayer)
