# core/display.py
import time

def welcome():
    print("\n*** Welcome to the Pokémon API ***")

def ask_draw():
    return input("\n> Do you want to draw a Pokémon? (y/n): ").strip().lower() == "y"

def draw_animation():
    print("\n**************************\n")
    print("Drawing a Pokémon, please wait...\n")
    for _ in range(3):
        print(".")
        time.sleep(2)

def say_goodbye():
    print("\n**************************")
    print("Goodbye, closing the program...")
    for _ in range(3):
        print(".")
        time.sleep(0.5)
    print("\nDone!")

def show_pokemon(p):
    print(f"\nID: {p['id']}")
    time.sleep(1)
    print(f"Name: {p['name']}")
    time.sleep(1)
    print(f"Height: {p['height']} cm")
    time.sleep(1)
    print(f"Weight: {p['weight']} kg")
    time.sleep(1)
    print("Types:")
    for t in p['types']:
        print(f" - {t}")
        time.sleep(1)
    print("Abilities:")
    for a in p['abilities']:
        print(f" - {a}")
        time.sleep(1)