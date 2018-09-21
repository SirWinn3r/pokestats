import requests

from constants import API_POKEMON_PATH
from constants import ERRMSG_API_MISC_ERROR
from constants import ERRMSG_API_UNKNOWN_POKEMON
from exceptions import APIError


def get_pokemon(pokemon_name):
    # Get the pokemon JSON object from the API
    pokemon_api_path = API_POKEMON_PATH % {"pokemon_name": pokemon_name}
    try:
        response = requests.get(pokemon_api_path)
        if response.ok:
            pokemon = response.json()
            return pokemon
        else:
            raise APIError(ERRMSG_API_UNKNOWN_POKEMON)
    except requests.exceptions.ConnectionError:
        raise APIError(ERRMSG_API_MISC_ERROR)
