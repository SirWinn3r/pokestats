API_PATH = "http://localhost:8000/api/v2/"
API_POKEMON_PATH = API_PATH + "pokemon/%(pokemon_name)s"

ERRMSG_API_ERROR = "/!\\ Aaaaaaaand it didn't work! (%s) /!\\"
ERRMSG_API_UNKNOWN_POKEMON = "Oh, it seems that pokemon does not exist..."
ERRMSG_API_MISC_ERROR = "Oops, something's wrong with the API, is it up?"

POKEMON_FORMATTED_STATS = """
Species: %(species)s
Height: %(height)s (ft)
Weight: %(weight)s (lbs)
Base experience points: %(base_experience)s (xp)
Types: %(types)s
Stats: %(stats)s
"""
