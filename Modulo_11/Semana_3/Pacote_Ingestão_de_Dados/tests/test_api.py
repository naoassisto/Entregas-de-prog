import pytest
from modulo.api import fetch_pokemon_data

def test_fetch_pokemon_data():
    data = fetch_pokemon_data('pikachu')
    assert data is not None
    assert data['name'] == 'pikachu'
