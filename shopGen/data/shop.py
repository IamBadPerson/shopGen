from tinydb import TinyDB, Query
from shopGen.data.base import BaseData

from shopGen.data.exceptions import ValidationException


class ShopData(BaseData):

    def __init__(self):
        super().__init__()
        self.update_table_name('SHOP')

    def insert(self, name: str, shopType: str, size: str, wealth: int):
        """
        Inserts new data into database table.
        """
        if self.table.contains(Query().name == name):
            raise ValidationException(
                f"a shop with the name of [{name}] already exists."
            )

        row = {
            "shop_name": name,  # name must be unique
            "shop_type": shopType,
            "shop_size": size,
            "shop_wealth": wealth,
            "shop_stats_supply": 0,
            "shop_stats_demand": 0,
            "shop_stats_stability": 0
        }

        # make changes for wealth
        if wealth > 0:
            row['shop_stats_supply'] += -1
            row['shop_stats_demand'] += 1
            row['shop_stats_stability'] -= 1
        
        if wealth > 3:
            row['shop_stats_stability'] += 0

        if wealth > 5:
            row['shop_stats_supply'] += 1
            row['shop_stats_stability'] += 1

        # make changes based on type
        match row['shop_type']:
            case "Apothecary":
                row['shop_stats_demand'] += 1
            case "General Merchant":
                row['shop_stats_supply'] -= 1
            case "Grocer":
                row['shop_stats_supply'] -= 1
            case "Blacksmith":
                row['shop_stats_demand'] -= 1

        # makes changes based on size
        match row['shop_size']:
            case 'tiny stall':
                row['shop_stats_stability'] -= 1
                row['shop_stats_supply'] -= 1
            case 'emporium':
                row['shop_stats_stability'] += 1
                row['shop_stats_supply'] += 1
            case 'caravan or tradeing post':
                row['shop_stats_stability'] += 1
                row['shop_stats_supply'] += 1

        return self.table.insert(row)
    



