"""
FOR LOCAL DEVELOPMENT ONLY!
This file will delete all objects from the database.
"""
import django
import os
from dotenv import load_dotenv

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'
load_dotenv("../../.env")

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'

# Set up the Django environment
django.setup()

from games.models import Game, Platform, Multiplayer

Platform.objects.all().delete()
Multiplayer.objects.all().delete()
Game.objects.all().delete()