import unittest

from unittest.mock import patch

from constants import ERRMSG_API_UNKNOWN_POKEMON
from exceptions import APIError
from pokestats import display_pokemon_stats
from pokestats import get_pokemon_stats

API_ERROR_UKNOWN_POKEMON = APIError(ERRMSG_API_UNKNOWN_POKEMON)
DUMMY_POKEMON = {
    "name": "Pikachu",
    "species": {"name": "pika"},
    "height": 5,
    "weight": 17,
    "base_experience": 456,
    "types": [
        {"type": {"name": "electric"}},
        {"type": {"name": "helicopter"}},
        {"type": {"name": "book"}}
    ],
    "stats": [
        {"stat": {"name": "spirit"}, "base_stat": 60},
        {"stat": {"name": "happiness"}, "base_stat": 100},
    ],
}
DUMMY_POKEMON_DISPLAYED_STATS = {
    "species": "pika",
    "height": 5,
    "weight": 17,
    "base_experience": 456,
    "types": "electric, helicopter, book",
    "stats": "spirit: 60; happiness: 100",
}
KNOWN_POKEMON_NAME = "Pikachu"
UNKNOWN_POKEMON_NAME = "Batman"


class TestPokestats(unittest.TestCase):
    @patch('pokestats.get_pokemon', side_effect=API_ERROR_UKNOWN_POKEMON)
    @patch('pokestats.display_error')
    def test_display_error_if_pokemon_is_unknown(self,
                                                 mock__display_error,
                                                 mock__get_pokemon):
        display_pokemon_stats(UNKNOWN_POKEMON_NAME)
        mock__get_pokemon.assert_called_once_with(UNKNOWN_POKEMON_NAME.lower())
        mock__display_error.assert_called_once_with(API_ERROR_UKNOWN_POKEMON)

    @patch('pokestats.get_pokemon', return_value=DUMMY_POKEMON)
    @patch('pokestats.get_pokemon_stats', return_value=DUMMY_POKEMON)
    @patch('pokestats.format_pokemon_stats')
    def test_display_error_if_pokemon_is_known(self,
                                               mock__format_pokemon_stats,
                                               mock__get_pokemon_stats,
                                               mock__get_pokemon):
        display_pokemon_stats(KNOWN_POKEMON_NAME)
        mock__get_pokemon.assert_called_once_with(KNOWN_POKEMON_NAME.lower())
        mock__get_pokemon_stats.assert_called_once_with(DUMMY_POKEMON)
        mock__format_pokemon_stats.assert_called_once_with(KNOWN_POKEMON_NAME,
                                                           DUMMY_POKEMON)

    def test_display_pokemon_stats(self):
        pokemon_stats = get_pokemon_stats(DUMMY_POKEMON)
        self.assertDictEqual(pokemon_stats, DUMMY_POKEMON_DISPLAYED_STATS)


if __name__ == "__main__":
    unittest.main()
