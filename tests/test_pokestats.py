from unittest.mock import patch

from pokestats import display_pokemon_stats

KNOWN_POKEMON_NAME = "Pikachu"
UNKNOWN_POKEMON_NAME = "Batman"


@patch('pokeapiservice.get_pokemon')
@patch('pokestats.display_unknown_pokemon')
def test_display_error_if_pokemon_is_unknown(
        mock__get_pokemon, mock__display_unknown_pokemon):
    display_pokemon_stats(UNKNOWN_POKEMON_NAME)
    mock__get_pokemon.assert_called_with(UNKNOWN_POKEMON_NAME.lower())
    mock__display_unknown_pokemon.assert_called_with(UNKNOWN_POKEMON_NAME)
