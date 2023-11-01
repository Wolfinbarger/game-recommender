from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.core.paginator import Paginator
from .models import Game

from django.utils.module_loading import import_module
igdb = import_module("services.igdb")


# Constants
OBJECTS_PER_PAGE = 10


def generate_paginator(query_set, request, objects_per_page=OBJECTS_PER_PAGE):
    page_number = request.GET.get("page")
    return Paginator(query_set, objects_per_page).get_page(page_number), page_number


def generate_http_400_response(error):
    response = HttpResponse(content=error)
    return HttpResponseBadRequest(response)


# GET /api/games
# Query Params
#  - page <int> required
def index(request):
    game_list = Game.objects.all().order_by("title")
    page, page_number = generate_paginator(game_list, request)

    if page_number is None:
        return generate_http_400_response("Query parameter 'page' missing.")

    data = [game.to_json() for game in page]

    # Enrich game data from database with IGDB data
    # igdb_api = igdb.IGDB()
    # for game in data:
    #     igdb_search_results = igdb_api.search(game.title)
    #     print(igdb_search_results[0].get('id'))

    # Ref: https://docs.djangoproject.com/en/4.2/ref/request-response/#jsonresponse-objects
    return JsonResponse({"page_number": page_number, "num_of_objects": OBJECTS_PER_PAGE, "data": data})
