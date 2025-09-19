import click
from shopGen.data.shop import ShopData
from shopGen.data.exceptions import ValidationException
from shopGen.http import importItems
from shopGen.shop import list_all_shops, get_all_docIds, shop_type_options
from shopGen.shop import showShop
from shopGen.common import import_master_price, importShards
from shopGen.data.main import truncateDatabase


@click.group()
def cli(): pass


@cli.command()
def reset():
    """deletes all data and import"""
    if click.confirm('This action will destory all of your data'):
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
        print(err)
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


if __name__ == '__main__':
    cli()
