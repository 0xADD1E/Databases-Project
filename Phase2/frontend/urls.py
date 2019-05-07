from django.urls import path
from .views import pokemon_view, typechart, matchup_uploader, kalos_uploader, pokemon_info, searchie_boi, stats_uploader
from collections import namedtuple
from typing import List, Dict
NavInfo = namedtuple('NavInfo', ['name', 'view', 'route'])
pages: List[NavInfo] = [
    NavInfo(name='Searchieboi', view=searchie_boi, route='/searchieboi'),
    NavInfo(name='Pokémon', view=pokemon_view, route='/'),
    NavInfo(name='Type Chart', view=typechart, route='/chart'),
    NavInfo(name='Upload Kalos', view=kalos_uploader, route='/kalos'),
    NavInfo(name='Upload Matchups', view=matchup_uploader, route='/matchup'),
    NavInfo(name='Upload Stats', view=stats_uploader, route='/stats'),
    NavInfo(name='Admin', view=None, route='/admin')
]
others: List[NavInfo] = [
    NavInfo(name='Pokemon Data', view=pokemon_info, route='/pkmn')
]


def nav_menu(request) -> Dict[str, List[NavInfo]]:
    return {'nav_links': pages}


page_patterns = [path(a.route.strip('/'), a.view, name=a.name) for a in pages if a.view]  # noqa
other_patterns = [path(a.route.strip('/'), a.view, name=a.name) for a in others if a.view]  # noqa
urlpatterns = page_patterns + other_patterns
