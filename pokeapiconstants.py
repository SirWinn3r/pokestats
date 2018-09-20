API_PATH = "http://localhost:8000/api/v2/"
API_POKEMON_PATH = API_PATH + "pokemon/%(pokemon_name)s"

ERRMSG_UNKNOWN_POKEMON = "/!\\ Sorry, I don't know any pokemon named %s! /!\\"

POKEMON_FORMATTED_STATS = """
Species: %(species)s
Height: %(height)s (ft)
Weight: %(weight)s (lbs)
Base experience points: %(base_experience)s (xp)
Types: %(types)s
Stats: %(stats)s
"""
