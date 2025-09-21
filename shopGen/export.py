import yaml
from pathlib import Path

from shopGen.data.shop import ShopData
# from shopGen.data.stock import 

class YamlExport:

    def __init__(self, output_path: str) -> None:
        self.path = output_path
        self.shop = ShopData()
        pass

    def create_ymal_object(self) -> str:
        obj = {
            "Location": "default",
            "Population": "default",
            "Shops": []
        }

        for shop in ShopData().all():
            row = {
                'name': shop['shop_name'],
                'size': shop['shop_type'],
                'wealth': shop['shop_wealth']
            }
            obj['Shops'].append(row)

        return yaml.dump(obj)
    
    def createFile(self):
        
        p = Path(self.path)
        print(p)

        p.write_text(self.create_ymal_object())

        return True





