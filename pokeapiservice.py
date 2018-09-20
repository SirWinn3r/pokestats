import requests

from pokeapiconstants import API_POKEMON_PATH


def get_pokemon(pokemon_name):
    # Get the pokemon JSON object from the API
    pokemon_api_path = API_POKEMON_PATH % {"pokemon_name": pokemon_name}
    response = requests.get(pokemon_api_path)
    if response.ok:
        pokemon = response.json()
        if pokemon.get("detail"):
            pokemon = None
    else:
        pokemon = None
    return pokemon
