# core/api.py
import requests
import json
import time
from core.display import show_pokemon
import metadata

POKEMON_LIST_PATH = "data/pokemon_list.json"

def get_basic_pokemon_info(pokemon_id, my_pokemon_list):
    url = metadata.BASE_URL + metadata.ENDPOINTS["pokemon"] + pokemon_id
    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.status_code)
        return

    data = response.json()

    pokemon_info = {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
    }

    show_pokemon(pokemon_info)
    my_pokemon_list.append(pokemon_info)

    with open(POKEMON_LIST_PATH, "w") as f:
        json.dump(my_pokemon_list, f, indent=4)

    print("\nPokémon saved to pokemon_list.json")