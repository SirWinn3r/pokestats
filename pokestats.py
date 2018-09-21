import argparse
import sys

from constants import ERRMSG_API_ERROR
from constants import POKEMON_FORMATTED_STATS
from exceptions import APIError
from service import get_pokemon


def display_pokemon_stats(pokemon_name):
    # Main function, start the whole thing!
    pokemon_name_lower = pokemon_name.lower()
    try:
        pokemon = get_pokemon(pokemon_name_lower)
        pokemon_stats = get_pokemon_stats(pokemon)
        format_pokemon_stats(pokemon_name, pokemon_stats)
    except APIError as err:
        display_error(err)


def display_error(errmsg):
    print(ERRMSG_API_ERROR % errmsg)


def format_pokemon_stats(pokemon_name, pokemon):
    # Display a given pokemon stats
    print("Stats for pokemon %s:" % pokemon_name)
    print(POKEMON_FORMATTED_STATS % pokemon)


def get_pokemon_stats(pokemon):
    # Extract only the stats we want to display and format some of them
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('pokemon_name', type=str)
    args = parser.parse_args(sys.argv[1:])
    display_pokemon_stats(args.pokemon_name)
