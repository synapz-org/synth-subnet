from synth.miner.price_simulation import get_asset_price

price = get_asset_price("BTC")
print(f"Current BTC Price: ${price:,.2f}")
