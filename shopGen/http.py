from pathlib import Path
from time import sleep
from json import loads

from requests import request
from rich.progress import track
from rich.console import Console

from shopGen.data.stock import StockData
from shopGen.common import convert_to_copper


def get(index: str, path: str = 'equipment'):
    url = f'https://www.dnd5eapi.co/api/2014/{path}/{index}'
    resp = request("GET", url=url, headers={
        'Accept': 'application/json'}, data={})
    return resp.text


def importItems(use_cache: bool = True):

    con = Console()
    file_path = 'data/e_list.json'
    doc_ids = []
    # get from api if use_cache is False and index file dose not exist
    if (use_cache is False) or (Path(file_path).is_file() is False):
        con.print('getting data from api.')
        url = 'https://www.dnd5eapi.co/api/2014/equipment'
        resp = request("GET", url=url, headers={
            'Accept': 'application/json'}, data={})

        data = resp.text

        #  write the cacheing file
        with open("data/e_list.json", mode='w') as f:
            f.write(data)

    else:
        con.print('useing file cache')
        with open('data/e_list.json', 'r') as f:
            data = f.read()

    jsonList = loads(data)

    stock_data = StockData()
    with con.status("[bold gree] Importing Equipment ...", spinner='earth') as status:
        jsonResultOn = 0
        for each in jsonList['results']:

            data = get(each['index'])
            json = loads(data)
            price = 0

            if 'weight' not in json.keys():
                json['weight'] = 0

            match json['cost']['unit']:
                case "gp":
                    price = convert_to_copper(gold=json['cost']['quantity'])
                case "sp":
                    price = convert_to_copper(silver=json['cost']['quantity'])
                case "cp":
                    price = convert_to_copper(copper=json['cost']['quantity'])

            doc_id = stock_data.insert(
                name=each['name'],
                type=json['equipment_category']['name'],
                weight=json['weight'],
                cost_cp=price)
            con.log(f"imported - {each['name']}")
            status.update(f"Importing Equipment {jsonResultOn} of {len(jsonList['results'])}")
            jsonResultOn += 1
            doc_ids.append(doc_id)
    return doc_ids
