from tinydb import TinyDB, Query
from shopGen.data.base import BaseData

from shopGen.data.exceptions import ValidationException


class ShopData(BaseData):

    def __init__(self):
        super().__init__()
        self.update_table_name('SHOP')

    def insert(self, name: str, shopType: str, size: str, wealth: int):
        if self.table.contains(Query().name == name):
            raise ValidationException(
                f"a shop with the name of [{name}] already exists."
            )

        return self.table.insert({
            "shop_name": name,  # name must be unique
            "shop_type": shopType,
            "shop_size": size,
            "shop_wealth": wealth       
        })


