
def price_calc(stock_base_price: int,  shop_supply: int, shop_demand: int, shop_stability: int):

    supply = (-0.05 * shop_supply)
    demand = (0.10 * shop_demand)
    stability = (-0.03 * shop_stability)

    multiplier = supply + demand + stability
    return stock_base_price * multiplier 


def copper_to_coins(copper: int) -> str:
    # conversion rates
    COPPER_PER_SILVER = 10
    SILVER_PER_GOLD = 10
    COPPER_PER_GOLD = COPPER_PER_SILVER * SILVER_PER_GOLD  # 100
    
    # calculate gold, silver, copper
    gold = copper // COPPER_PER_GOLD
    remainder = copper % COPPER_PER_GOLD
    silver = remainder // COPPER_PER_SILVER
    copper = remainder % COPPER_PER_SILVER
    
    # build result string
    parts = []
    if gold:
        parts.append(f"{gold} gold")
    if silver:
        parts.append(f"{silver} silver")
    if copper:
        parts.append(f"{copper} copper")
    
    return ", ".join(parts) if parts else "0 copper"
