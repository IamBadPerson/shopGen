import click
from tinydb import Query
from loguru import logger
from shopGen.data.shop import ShopData
from shopGen.data.stock import StockData
from shopGen.data.exceptions import ValidationException
from shopGen.http import importItems
from shopGen.shop import list_all_shops, get_all_docIds, shop_type_options
from shopGen.shop import showShop
from shopGen.common import import_master_price, importShards, create_table_from_rows
from shopGen.data.main import truncateDatabase
from shopGen.stock import copper_to_coins

logger.add('data/log/file_shopgen.log', format="{time} {level} {message}", level="INFO")

@click.group()
def cli(): pass


@cli.command()
def reset():
    """deletes all data and import"""
    if click.confirm('This action will destory all of your data'):
        logger.info("starting a reset.")
        truncateDatabase()
        import_master_price()
        importItems()
        importShards()


@cli.group()
def shop():
    """
    Handles the main functionality for the shop application.
    This function serves as the entry point for shop-related operations.
    Currently, it is a placeholder and does not implement any logic.
    Returns:
        None
    """
    pass


shop_size_options = [
    "tiny stall",
    "small",
    "medium",
    "large",
    "emporium",
    "caravan or tradeing post"]


@shop.command()
@click.argument('name', type=str)
@click.argument('shop_type', type=click.Choice(shop_type_options))
@click.argument('size', type=click.Choice(shop_size_options))
@click.argument('wealth', type=click.IntRange(1, 6))
def create(name, shop_type, size, wealth):
    """creates a shop"""
    try:
        shopObj = ShopData()
        shopObj.insert(
            name=name,
            shopType=shop_type,
            size=size,
            wealth=wealth
        )
    except ValidationException as err:
        logger.error(err)
    pass


@shop.command()
def list():
    list_all_shops()
    pass


@shop.command()
@click.argument('shop_id', type=click.Choice(ShopData().read_all_ids()))
def see(shop_id):
    """shows a single shop in a useable format"""
    showShop(shop_id)


@shop.command()
@click.argument('uid', type=click.Choice(get_all_docIds()))
def remove(uid):
    if click.confirm(f"remove shop with a id of {uid}?"):
        shopObj = ShopData()
        shopObj.remove_by_id(uid)

@cli.group()
def stock():
    """
    stock is the items by the shop.
    """
    pass

@stock.command()
@click.argument("name", type=str,)
@click.argument('type', type=click.Choice(StockData().get_all_types()))
@click.argument('weight', type=int)
@click.argument('cost_cp', type=int)
def create(name: str, type: str, weight: int, cost_cp: int):
    """creates a new stock item"""
    obj = StockData()
    return obj.insert(
        name=name,
        type=type,
        weight=weight,
        cost_cp=cost_cp
    )

@stock.command()
@click.option('--key', type=click.Choice(['name', 'type', '']), default='')
@click.option('--value', type=str, default='')
def list(key: str, value: str):
    if len(key) > 0:
        data = StockData().table.search(Query()[key] == value)
    else:
        data = StockData().all()

    # convert prices to usable prices
    for each in data:
        each['cost_cp'] = copper_to_coins(each['cost_cp'])
    create_table_from_rows(data)

@stock.command()
@click.argument('doc_id', type=int)
def remove(doc_id):
    if click.confirm("are you sure?"):
        StockData().remove_by_id(doc_id)


if __name__ == '__main__':
    cli()
