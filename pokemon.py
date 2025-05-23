""" This script fetches Pokémon data from the Pokémon API and saves it to a JSON file. """
import time
import json
import random
import requests
import metadata
import my_pokemons


print("\n*** Welcome to the Pokémon API ***")

FLAG = True # Flag to control the loop


# Get the Pokémon list from the API
def get_basic_pokemon_info(pokemon_id, my_pokemon_list):
    """
    Fetches basic information about a Pokémon from the API and saves it to a JSON file.
    """
    url = (
        metadata.BASE_URL + metadata.ENDPOINTS["pokemon"] + pokemon_id
    )  # Base URL + Pokémon endpoint + Pokémon ID
    response = requests.get(url, timeout=10)  # Pokémon API request

    # Check if the response is successful
    if response.status_code != 200:
        print("Error:", response.status_code)
        return

    # Saving the response to a JSON file
    data = response.json()

    print(f"\nID : {data['id']}")
    time.sleep(1)
    print(f"Name : {data['name']}")
    time.sleep(1)
    print(f"Height : {data['height']} cm")
    time.sleep(1)
    print(f"Weight : {data['weight']} kg")
    time.sleep(1)
    print("Types : ")
    time.sleep(1)
    for t in data["types"]:
        print(f" - {t['type']['name']}")
        time.sleep(1)
    print("Abilities : ")
    time.sleep(1)
    for a in data["abilities"]:
        print(f" - {a['ability']['name']}")
        time.sleep(1)

    pokemon_info = {
        "id": data["id"],
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
    }

    my_pokemon_list.append(pokemon_info)  # Add the Pokémon info to the list
    time.sleep(1)

    # Save the Pokémon info to a JSON file
    with open("pokemon_list.json", "w", encoding="utf-8") as f:
        json.dump(my_pokemon_list, f, indent=4)
    print("\nPokémon saved to pokemon_list.json")


# Interactive loop to ask the user if they want to draw a Pokémon
while FLAG:
    is_draw = (
        input("\n> Do you want to draw a Pokémon? (y/n): ").strip().lower()
    )  # Ask the user if they want to draw a Pokémon

    # Check if the user input is valid
    if is_draw == "y":  # If the user wants to draw a Pokémon

        print("\n**************************\n")
        time.sleep(1)
        print("Drawing a Pokémon, please wait...\n")
        for i in range(3, 0, -1):
            print(".")
            time.sleep(2)

        RANDOM_NUM = random.randint(
            1, metadata.POKEMON_COUNT
        )  # Generate a random Pokémon ID

        #RANDOM_NUM = 788  # For testing purposes, set a specific Pokémon ID

        pokemon_list = my_pokemons.find_pokemon(
            RANDOM_NUM
        )  # Call the function to find a Pokémon with the random ID

        if pokemon_list:  # If the Pokémon is not found
            print("\n**************************")
            print(f"\nPokémon ID: {RANDOM_NUM}\n")
            time.sleep(1)
            print("Fetching Pokémon info from the API...\n")

            for i in range(3, 0, -1):
                print(".")
                time.sleep(2)

            get_basic_pokemon_info(
                str(RANDOM_NUM), pokemon_list
            )  # Call the function to get Pokémon info with the random ID

    else:  # If the user doesn't want to draw a Pokémon
        print("\nOk goodbye!")

    # Ask the user if they want to continue or exit
    FLAG = input("\n> Do you want to continue? (y/n): ").strip().lower() == "y"
    if not FLAG:  # If the user doesn't want to continue
        print("\n**************************")
        print("Goodbye, closing the program...")

        for i in range(3, 0, -1):
            print(".")
            time.sleep(0.5)

        print("\nDone!")
        # break  # End of the program
        FLAG = False
