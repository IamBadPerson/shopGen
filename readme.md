# README.md for Shop Gen

# Shop Gen 🏪
# *A shop generator for tabletop role-playing games (TTRPGs)*

"""
`shop-gen` is a Python project that creates **shop front-ends** for use in TTRPG campaigns. It is designed to give Dungeon Masters and game developers quick, believable shops with inventories, sizes, and wealth levels, ready to present to players.

Repository: https://github.com/IamBadPerson/shopGen
"""

## Features
"""
- 🏷️ Shop Types – Bakers, blacksmiths, taverns, apothecaries, and more.
- 📦 Inventories – Items mapped to each shop type (food, tools, weapons, services, etc).
- 📊 Shop Details – Size, wealth, and specialties generated automatically.
- 📜 Readable Outputs – Produces clear shop sheets you can show directly to players.
- ⚙️ Flexible System – Easy to extend with new shop types, items, or regional economies.
"""

## Installation
"""
git clone https://github.com/IamBadPerson/shopGen.git
cd shopGen
pip install -r requirements.txt
"""

## Usage
"""
python shopgen.py
"""
Generates a shop with:
- Name (randomly generated)
- Shop Type (e.g., Blacksmith, Grocer)
- Size (tiny stall → emporium)
- Wealth level (poor → wealthy)
- Inventory list

Example Output:
"""
🛠️ The Iron Anvil
Type: Blacksmith
Size: Medium
Wealth: Comfortable

Items for Sale:
- Longsword (15 gp)
- Hammer (1 gp)
- Shield (10 gp)
"""

## Data Model
"""
Shop Types: Defined in `shop_item_map`, each shop maps to one or more item categories.

Example:
shop_item_map = {
    "Baker": ["Food"],
    "Butcher": ["Food"],
    "Blacksmith": ["Tools", "Weapons", "Armor"],
    "Apothecary": ["Substance", "Herbs"],
    "Tavern": ["Food", "Service"]
}

Item Classes: Food, Tools, Weapons, Armor, Service, Substance

Shop Attributes:
- Name: generated
- Type: matches `shop_item_map` key
- Size: tiny stall, small, medium, large, emporium, caravan or trading post
- Wealth: abstracted economic level (poor → wealthy)
"""

## Language
"""
- Shop types = real-world names (e.g., Baker, Butcher)
- Item classes = plain descriptors (Food, Tools, etc.)
- Output = written in plain English for immediate DM use

Custom language or fantasy naming can be done by editing `shop_item_map` or naming modules.
"""

## Roadmap
"""
- [ ] Add regional economic modifiers
- [ ] Introduce rarity scaling
- [ ] Export shops to CSV/JSON for reuse
- [ ] Web interface for player-facing shop sheets
"""

## License
"""
MIT License – free to use, modify, and share.
"""
