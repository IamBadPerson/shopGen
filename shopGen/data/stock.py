from shopGen.data.base import BaseData

from tinydb import Query


class StockData(BaseData):

    def __init__(self):
        super().__init__()
        self.update_table_name('stock')

    def insert(self, name: str, type: str, weight: int, cost_cp: int):

        return self.table.insert({
            'name': name,
            'type': type,
            'weight': weight,
            'cost_cp': cost_cp
        })

    def get_all_types(self):

        s_types = []
        for e in self.all():
            if e['type'] not in s_types:
                s_types.append(e['type'])
        return s_types

    def get_by_stock(self, stock_type: str):
        qry = Query()
        return self.table.search(qry.type == stock_type)
