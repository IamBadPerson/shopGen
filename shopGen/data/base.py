from tinydb import TinyDB


class BaseData():

    def __init__(self, path: str = 'data/ds.json') -> None:
        self.db = TinyDB(path)
        self.table = self.db.table(__name__)
        self.update_table_name()  # used to define self.table

    def update_table_name(self, name: str = __name__):
        self.table = self.db.table(name)
        return True

    def all(self):
        return self.table.all()

    def remove_by_id(self, uid: int):
        return self.table.remove(doc_ids=[uid])
    
    def read_by_id(self, uid: int):
        return self.table.get(doc_id=uid)
    
    def read_all_ids(self):
        doc_ids = []
        for each in self.table.all():
            doc_ids.append(each.doc_id)
        return doc_ids
    
    def truncate(self):
        return self.table.truncate()