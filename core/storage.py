"""
    Storage module for Pokémon data management.
    This module provides functions to load Pokémon data from a JSON file,
    check for duplicates, and manage the Pokémon list.
"""
import json
import time

POKEMON_LIST_PATH = "data/pokemon_list.json"


def load_pokemon_list():
    """
    Load the Pokémon list from a JSON file.
    """
    try:
        with open(POKEMON_LIST_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def check_duplicate(pokemon_id, data):
    """
        Check if a Pokémon with the given ID already exists in the list.
    """
    for pokemon in data:
        if str(pokemon["id"]) == pokemon_id:
            print("\n~~~ You already have this Pokémon ~~~")
            time.sleep(1)
            print(f"\nName: {pokemon['name']}")
            return True
    print("\nYou don't have this Pokémon :(")
    time.sleep(1)
    return False
