""" Look for a Pokémon in the list """

import time
import json


def find_pokemon(pokemon_id):
    """
    Check if a Pokémon is already in the list.
    """
    with open("pokemon_list.json", "r", encoding="utf-8") as f:
        data = json.load(f)

        for pokemon in data:
            if pokemon["id"] == pokemon_id:
                print("\n~~~ You already have this Pokémon ~~~")
                time.sleep(1)
                print(f"\nName: {pokemon['name']}")
                time.sleep(1)
                print(f"ID: {pokemon['id']}")
                time.sleep(1)
                print(f"Height: {pokemon['height']} cm")
                time.sleep(1)
                print(f"Weight: {pokemon['weight']} kg")
                time.sleep(1)
                print("Types: ")
                time.sleep(1)
                for t in pokemon['types']:
                    print(f" - {t}")
                    time.sleep(1)
                print("Abilities: ")
                time.sleep(1)
                for a in pokemon['abilities']:
                    print(f" - {a}")
                    time.sleep(1)
                return False
    print("\nYou don't have this Pokémon :(\n")
    time.sleep(1)
    return data
