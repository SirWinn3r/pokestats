import argparse
import requests
import sys

API_PATH = "http://localhost:8000/api/v2/"
API_POKEMON_PATH = API_PATH + "pokemon/%(pokemon_name)s"
POKEMON_FORMATTED_STATS = """
Species: %(species)s
Height: %(height)s (ft)
Weight: %(weight)s (lbs)
Base experience points: %(base_experience)s (xp)
Types: %(types)s
Stats: %(stats)s
"""


def display_pokemon_stats(pokemon_name):
    pokemon_name_lower = pokemon_name.lower()
    pokemon = get_pokemon(pokemon_name_lower)
    pokemon_stats = get_pokemon_stats(pokemon)
    format_pokemon_stats(pokemon_name, pokemon_stats)


def format_pokemon_stats(pokemon_name, pokemon):
    print("Stats for pokemon %s:" % pokemon_name)
    print(POKEMON_FORMATTED_STATS % pokemon)


def get_pokemon(pokemon_name):
    pokemon_api_path = API_POKEMON_PATH % {"pokemon_name": pokemon_name}
    response = requests.get(pokemon_api_path)
    pokemon = response.json()
    return pokemon


def get_pokemon_stats(pokemon):
    types = ", ".join(map(lambda t: t["type"]["name"], pokemon["types"]))
    stats = "; ".join(
        map(lambda s: "%s: %s" % (s["stat"]["name"], s["base_stat"]),
            pokemon["stats"])
    )
    pokemon_stats = {
        "species": pokemon["species"]["name"],
        "height": pokemon["height"],
        "weight": pokemon["weight"],
        "base_experience": pokemon["base_experience"],
        "types": types,
        "stats": stats,
    }
    return pokemon_stats


parser = argparse.ArgumentParser()
parser.add_argument('pokemon_name', type=str)
args = parser.parse_args(sys.argv[1:])

display_pokemon_stats(args.pokemon_name)
