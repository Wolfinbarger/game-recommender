from json import JSONDecoder
from django.http import JsonResponse
from .models import Game


def index(request):
    data = [game.to_json() for game in Game.objects.all()]

    # Ref: https://docs.djangoproject.com/en/4.2/ref/request-response/#jsonresponse-objects
    return JsonResponse({"data": data})


def fake_index(request):
    with open('../../data/fake_games_dataset.json', 'r') as data:
        data = JSONDecoder().decode(data.read())

        return JsonResponse({"data": data})
