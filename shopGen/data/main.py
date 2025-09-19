from shopGen.data.shop import ShopData
from shopGen.data.stock import StockData

def truncateDatabase():
    StockData().truncate()
    ShopData().truncate()
