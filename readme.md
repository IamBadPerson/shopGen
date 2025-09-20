# Shop Gen 🏪  
*A shop generator for tabletop role-playing games (TTRPGs)*  

`shop-gen` is a Python project that creates **shop front-ends** for use in TTRPG campaigns. It is designed to give Dungeon Masters and game developers quick, believable shops with inventories, sizes, and wealth levels, ready to present to players.  

📦 Repository: [IamBadPerson/shopGen](https://github.com/IamBadPerson/shopGen)  

---

## ✨ Features  
- 🏷️ **Shop Types** – Bakers, blacksmiths, taverns, apothecaries, and more.  
- 📦 **Inventories** – Items mapped to each shop type (food, tools, weapons, services, etc).  
- 📊 **Shop Details** – Size, wealth, and specialties generated automatically.  
- 📜 **Readable Outputs** – Produces clear shop sheets you can show directly to players.  
- ⚙️ **Flexible System** – Easy to extend with new shop types, items, or regional economies.  

---

## 📥 Installation  
Clone the repository and install dependencies:  

```bash
git clone https://github.com/IamBadPerson/shopGen.git
cd shopGen
pip install -r requirements.txt
```

---

## 🚀 Usage  

### Generate a Shop
```bash
python shopgen.py
```

This will generate a shop with:  
- **Name** (randomly generated)  
- **Shop Type** (e.g., Blacksmith, Grocer)  
- **Size** (tiny stall → emporium)  
- **Wealth level** (poor → wealthy)  
- **Inventory list**  

### Example Output
```
🛠️ The Iron Anvil
Type: Blacksmith
Size: Medium
Wealth: Comfortable

Items for Sale:
- Longsword (15 gp)
- Hammer (1 gp)
- Shield (10 gp)
```

---

## 🧾 Index of Commands

| Command | Description |
|----------|-------------|
| `python shopgen.py reset` | Deletes all shop data and re-imports from sources |
| `python shopgen.py shop create <name> <shop_type> <size> <wealth>` | Creates a new shop with given parameters |
| `python shopgen.py shop list` | Lists all existing shops |
| `python shopgen.py shop see <shop_id>` | Displays a single shop in a player-usable format |
| `python shopgen.py shop remove <uid>` | Removes a shop by its unique ID |

> 💡 Run `python shopgen.py --help` or `python shopgen.py <command> --help` to view detailed options.

## 🗂️ Data Model  

The generator works by combining **shop types**, **item classes**, and **shop attributes**.  

### Shop Types  
Defined in `shop_item_map`, each shop maps to one or more **item categories**:  

```python
shop_item_map = {
    "Baker": ["Food"],
    "Butcher": ["Food"],
    "Blacksmith": ["Tools", "Weapons", "Armor"],
    "Apothecary": ["Substance", "Herbs"],
    "Tavern": ["Food", "Service"],
    ...
}
```

### Item Classes  
Items are grouped into broad categories:  
- `Food` – bread, meat, ale, fish, etc.  
- `Tools` – hammers, saws, chisels.  
- `Weapons` – swords, axes, bows.  
- `Armor` – shields, chainmail, helmets.  
- `Service` – lodging, stabling, healing.  
- `Substance` – potions, poisons, alchemical goods.  

### Shop Attributes  
Each generated shop also has metadata:  
- **Name** – created using a naming function.  
- **Type** – matches one of the keys in `shop_item_map`.  
- **Size** – one of:  
  - `tiny stall`  
  - `small`  
  - `medium`  
  - `large`  
  - `emporium`  
  - `caravan or trading post`  
- **Wealth** – an abstracted economic level (poor → wealthy), affecting inventory depth.  

---

## 🌍 Language  

The project uses **clear English labels** for categories and items:  
- Shop types = real-world names (e.g., *Baker*, *Butcher*).  
- Item classes = plain descriptors (e.g., *Food*, *Tools*).  
- Output = written in plain English so DMs can drop it directly into games.  

> 💡 To customize the language (e.g., “Elven Bowyer” instead of “Bowyer”), edit the naming module or `shop_item_map`.  

---

## 📚 Roadmap  
- [ ] Add regional economic modifiers  
- [ ] Introduce rarity scaling  
- [ ] Export shops to CSV/JSON for reuse  
- [ ] Web interface for player-facing shop sheets  

---

## 📜 License  
MIT License – free to use, modify, and share.
