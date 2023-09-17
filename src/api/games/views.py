from json import JSONDecoder
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Game

# Constants
OBJECTS_PER_PAGE = 10


# Helper Method
def page(query_set, request, objects_per_page=OBJECTS_PER_PAGE):
    page_number = request.GET.get("page")
    return Paginator(query_set, objects_per_page).get_page(page_number), page_number


# GET /api/games
def index(request):
    game_list = Game.objects.all()
    page_obj, page_number = page(game_list, request)
    data = [game.to_json() for game in page_obj]

    # Ref: https://docs.djangoproject.com/en/4.2/ref/request-response/#jsonresponse-objects
    return JsonResponse({"page_number": page_number, "num_of_objects": OBJECTS_PER_PAGE, "data": data})


# GET /api/games/fake
def fake_index(request):
    game_list = Game.objects.all()
    page_obj, page_number = page(game_list, request)
    print(page_obj.object_list)

    with open('../../data/fake_games_dataset.json', 'r') as data:
        data = JSONDecoder().decode(data.read())

        return JsonResponse({"data": data})
