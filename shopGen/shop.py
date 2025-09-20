from random import choices, randint
from rich.layout import Layout
from rich.markdown import Markdown
from rich.columns import Columns
from rich.panel import Panel
from rich.console import Console
from loguru import logger
from shopGen.data.shop import ShopData
from shopGen.data.stock import StockData
from shopGen.common import create_table_from_rows
from shopGen.stock import copper_to_coins, price_calc


shop_item_map = {
    # Essential
    "Baker": ["Food"],
    "Butcher": ["Food"],
    "Brewer": ["Food"],
    "Fishmonger": ["Food"],
    "Grocer": ["Food", "Substance"],
    "Innkeeper": ["Service", "Food"],
    "Tavern": ["Service", "Food"],
    "Blacksmith": ["Tools", "Weapon", "Armor"],
    "General Merchant": ["Adventuring Gear", "Tools", "Food"],

    # Nice to Have
    "Dairyman": ["Food"],
    "Cheesemaker": ["Food"],
    "Cook": ["Food"],
    "Pastry Chef": ["Food"],
    "Tanner": ["Substance", "Armor"],
    "Cobbler": ["Clothing"],
    "Saddler": ["Mounts and Vehicles", "Clothing"],
    "Housewright": ["Furnishing"],
    "Wheelwright": ["Mounts and Vehicles", "Tools"],
    "Furniture Maker": ["Furnishing"],
    "Tailor": ["Clothing"],
    "Weaver": ["Clothing"],
    "Rope Maker": ["Tools", "Mounts and Vehicles"],
    "Healer": ["Service", "Substance"],
    "Barber-Surgeon": ["Service"],
    "Apothecary": ["Substance", "Service"],
    "Teamster": ["Service"],
    "Porter": ["Service"],
    "Messenger": ["Service"],
    "Guard": ["Service"],
    "Mercenary": ["Service", "Weapon", "Armor"],
    "Builder": ["Furnishing"],
    "Mason": ["Furnishing"],

    # Everything Else
    "Vintner": ["Food"],
    "Spice Seller": ["Food", "Substance"],
    "Silversmith": ["Furnishing", "Container"],
    "Goldsmith": ["Furnishing", "Container"],
    "Tinsmith": ["Tools", "Container"],
    "Purse Maker": ["Container", "Clothing"],
    "Scabbard Maker": ["Container", "Weapon"],
    "Shipwright": ["Mounts and Vehicles", "Tools"],
    "Toy Maker": ["Furnishing"],
    "Potter": ["Container", "Furnishing"],
    "Sculptor": ["Furnishing"],
    "Brickmaker": ["Furnishing"],
    "Glassblower": ["Container", "Furnishing"],
    "Rug Maker": ["Furnishing"],
    "Dyer": ["Clothing"],
    "Paper Maker": ["Furnishing"],
    "Candle Maker": ["Substance"],
    "Soapmaker": ["Substance"],
    "Bookbinder": ["Furnishing", "Service"],
    "Scribe": ["Service"],
    "Sage": ["Service"],
    "Teacher": ["Service"],
    "Scholar": ["Service"],
    "Prostitute": ["Service"],
    "Entertainer": ["Service"],
    "Musician": ["Service"],
    "Actor": ["Service"],
    "Bard": ["Service"],
    "Fortune Teller": ["Service"],
    "Diviner": ["Service"],
    "Hostler": ["Mounts and Vehicles", "Service"],
    "Miner": ["Substance"],
    "Prospector": ["Substance"],
    "Furrier": ["Clothing"],
    "Skinner": ["Clothing", "Substance"],
    "Moneylender": ["Service"],
    "Pawnbroker": ["Service", "Adventuring Gear"],
    "Enchanter": ["Weapon", "Armor", "Tools", "Adventuring Gear"],
    "Magic Component Seller": ["Substance", "Adventuring Gear"],
    "Potion Brewer": ["Substance", "Adventuring Gear"],
    "Sailor": ["Service"],
    "Ship Captain": ["Service"],
    "Architect": ["Service", "Furnishing"],

    "Bakers & Pastries": ["Food"]
}

shop_type_options = shop_item_map.keys()


def list_all_shops():

    data = ShopData().all()
    create_table_from_rows(data)


def get_all_docIds():

    data = []
    for row in ShopData().all():
        data.append(row.doc_id)

    return data


def build_shop(doc_id: int):
    shopObj = ShopData()
    stockObj = StockData()
    shop = shopObj.read_by_id(doc_id)

    if 'shop_type' not in shop.keys():
        logger.debug("shop type not found")
        return False

    item_subList = []
    itemTypes = shop_item_map[shop['shop_type']]

    for each in itemTypes:
        item_subList = item_subList + stockObj.get_by_stock(each)

    stock = []
    match shop['shop_size']:
        case "tiny stall":
            stock = choices(population=item_subList, k=randint(1, 6))
        case "small":
            stock = choices(population=item_subList, k=randint(7, 12))
        case "medium":
            stock = choices(population=item_subList, k=randint(13, 20))
        case "large":
            stock = choices(population=item_subList, k=randint(21, 28))
        case "emporium":
            stock = choices(population=item_subList, k=randint(29, 36))
        case "caravan or tradeing post":
            stock = choices(population=item_subList, k=randint(25, 32))

    shop['stock'] = stock
    return shop


def showShop(shop_id: int):
    sData = build_shop(shop_id)

    stockItems = []
    for each in sData['stock']:
        price = price_calc(
            each['cost_cp'],
            shop_supply=sData['shop_stats_supply'],
            shop_demand=sData['shop_stats_demand'],
            shop_stability=sData['shop_stats_stability'])
        rendString = Panel(
            f"{each.doc_id}  {each['name']} - \n {copper_to_coins(each['cost_cp'])}", width=40, height=5)
        stockItems.append(rendString)

    layout = Layout()
    layout.split_column(
        Layout(name="ShopInfo", size=10),
        Layout(name="Stock", size=30)
    )
    md = Markdown(f"""
# {sData['shop_name']}
### type: {sData['shop_type']}
### size: {sData['shop_size']}
""")
    layout['ShopInfo'].update(md)
    cols = Columns(stockItems, equal=True, expand=True)
    layout['Stock'].update(Panel(cols))
    Console().print(layout)
    return True
