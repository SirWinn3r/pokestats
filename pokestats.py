import argparse
import sys

from pokeapiconstants import ERRMSG_UNKNOWN_POKEMON
from pokeapiconstants import POKEMON_FORMATTED_STATS
from pokeapiservice import get_pokemon


def display_pokemon_stats(pokemon_name):
    # Main function
    pokemon_name_lower = pokemon_name.lower()
    pokemon = get_pokemon(pokemon_name_lower)
    if pokemon is not None:
        pokemon_stats = get_pokemon_stats(pokemon)
        format_pokemon_stats(pokemon_name, pokemon_stats)
    else:
        display_unknown_pokemon(pokemon_name)


def display_unknown_pokemon(pokemon_name):
    print(ERRMSG_UNKNOWN_POKEMON % pokemon_name)


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


parser = argparse.ArgumentParser()
parser.add_argument('pokemon_name', type=str)
args = parser.parse_args(sys.argv[1:])

display_pokemon_stats(args.pokemon_name)
