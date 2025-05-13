# core/storage.py
import json
import time

POKEMON_LIST_PATH = "data/pokemon_list.json"

def load_pokemon_list():
    try:
        with open(POKEMON_LIST_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def check_duplicate(pokemon_id, data):
    for pokemon in data:
        if str(pokemon["id"]) == pokemon_id:
            print("\n~~~ You already have this Pokémon ~~~")
            time.sleep(1)
            print(f"\nName: {pokemon['name']}")
            return True
    print("\nYou don't have this Pokémon :(")
    time.sleep(1)
    return False