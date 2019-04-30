from django.urls import path
from .views import pokemon_view, kalos_uploader
from collections import namedtuple
from typing import List, Dict
NavInfo = namedtuple('NavInfo', ['name', 'view', 'route'])
pages: List[NavInfo] = [
    NavInfo(name='Pokémon', view=pokemon_view, route='/'),
    NavInfo(name='Upload Data', view=kalos_uploader, route='/kalos'),
    NavInfo(name='Admin', view=None, route='/admin'),
]
others: List[NavInfo] = [

]


def nav_menu(request) -> Dict[str, List[NavInfo]]:
    return {'nav_links': pages}


page_patterns = [path(a.route.strip('/'), a.view, name=a.name) for a in pages if a.view]  # noqa
other_patterns = [path(a.route.strip('/'), a.view, name=a.name) for a in others if a.view]  # noqa
urlpatterns = page_patterns + other_patterns
