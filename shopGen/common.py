from pathlib import Path
from csv import reader, DictReader
from tinydb.table import Document
from rich.table import Table
from rich.console import Console

from shopGen.data.stock import StockData
from shopGen.data.shop import ShopData


def create_table_from_rows(list_docs: list[Document]):
    tbl = Table()
    headers = ["doc_id"]
    tbl.add_column("ids")

    for each in list_docs:
        # check the keys
        for k in each.keys():
            if k not in headers:
                headers.append(k)
                tbl.add_column(k)

    for each in list_docs:
        x = [str(each.doc_id)]
        for v in each.values():
            x.append(str(v))

        tbl.add_row(*x)

    Console().print(tbl)
    return tbl


def convert_to_copper(gold=0, silver=0, copper=0):
    """
    Converts gold, silver, and copper into total copper pieces.
    1 Gold = 100 Copper
    1 Silver = 10 Copper
    """

    total_copper = (gold * 100) + (silver * 10) + copper
    return total_copper


def import_master_price():
    stockTable = StockData()
    p = Path('data\\MasterPriceList.csv')
    if p.is_file() is False:
        return False

    with p.open('r') as fileObj:
        csv = DictReader(fileObj)
        for e in csv:
            value = e['Base Cost']
            if isinstance(value, str):
                try:
                    value = int(float(value.replace(",", "")))
                except BaseException:  # any problems just move on
                    with open('data/log.txt', mode='a') as file:
                        file.write(str(e))
                        value = 0
                    continue
            
            stockTable.insert(
                name=e['Item'],
                type=e['Class'],
                weight=0,
                cost_cp=convert_to_copper(silver=value)
            )


def importShards():
    p = Path('data/')
    shopObj = ShopData()
    files = p.iterdir()
    for file in list(files):
        if 'shops_shard.csv' in file.name:
            with file.open('r') as fileObj:
                csv = DictReader(fileObj)
                for each in csv:
                    try:
                        if isinstance(each['wealth'], str):
                            each['wealth'] = int(float(each['wealth'].replace(",", "")))
                        shopObj.insert(name=each['name'], shopType=each['shop_type'], size=each['size'], wealth=each['wealth'])
                    except TypeError:
                        with open('data\\log.txt', mode='a') as fObj:
                            fObj.write(str(each))
                            continue
