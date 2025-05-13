# Pokémon API Explorer

A terminal-based Python project that fetches and stores Pokémon data using the [PokeAPI](https://pokeapi.co/). Draw random Pokémon, check if you've already captured them, and save your collection locally.

---

## 🚀 Features

- Fetch Pokémon info from PokeAPI
- Store collected Pokémon in a local JSON file
- Prevent duplicate entries with local checks
- Display Pokémon details with a loading effect
- Easy customization and extension via modular design

---

## 🗂 Project Structure

```bash
├── pokemon.py           # Main script: controls flow, fetches data, saves to file
├── my_pokemons.py       # Helper: checks if Pokémon already exists in collection
├── metadata.py          # Contains API endpoints and base URL
├── pokemon_list.json    # Stored Pokémon collection
├── dartrix_info.json    # Example: individual Pokémon data format
├── .gitignore           # Standard Python ignores
```

---

## 🧪 How It Works

1. **Launch the program** via `python pokemon.py`
2. Choose to draw a new Pokémon.
3. If not already in your collection, fetch data from PokeAPI.
4. Show details with animations.
5. Save the Pokémon to `pokemon_list.json`.

---

## 📦 Requirements

Install dependencies:

```bash
pip install requests
```

---

## 🔧 Customization

- Modify `metadata.py` to expand API usage.
- Change hardcoded test ID (`random_num = 788`) to `random.randint(...)` for full randomness.

---

## 📁 Sample Output

```
ID: 788
Name: tapu-fini
Height: 13 cm
Weight: 212 kg
Types:
 - water
 - fairy
Abilities:
 - misty-surge
 - telepathy
```

---

## ✅ Future Ideas

- Add CLI arguments for specific Pokémon
- GUI version using tkinter or PyQt
- Filtering by type, ability, or generation
