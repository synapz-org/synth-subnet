from synth.miner.price_simulation import (
    simulate_crypto_price_paths,
    get_asset_price,
)
from synth.utils.helpers import convert_prices_to_time_format
import numpy as np

def calculate_volatility_regime(asset="BTC", window=12):
    """Calculate current volatility regime from recent prices"""
    prices = []
    for _ in range(window):
        price = get_asset_price(asset)
        if price:
            prices.append(price)
    returns = np.diff(np.log(prices))
    current_vol = np.std(returns) * np.sqrt(252)
    return current_vol

def generate_simulations(
    asset="BTC",
    start_time=None,
    time_increment=300,
    time_length=86400,
    num_simulations=1,
):
    """
    Generate simulated price paths with volatility clustering and adaptive momentum.
    """
    if start_time is None:
        raise ValueError("Start time must be provided.")

    current_price = get_asset_price(asset)
    if current_price is None:
        raise ValueError(f"Failed to fetch current price for asset: {asset}")

    # Calculate current volatility regime
    vol_regime = calculate_volatility_regime(asset)
    
    # Adjust base volatility based on current market conditions
    base_sigma = 0.01
    adjusted_sigma = base_sigma * (1 + vol_regime)

    simulations = simulate_crypto_price_paths(
        current_price=current_price,
        time_increment=time_increment,
        time_length=time_length,
        num_simulations=num_simulations,
        sigma=adjusted_sigma,
    )

    predictions = convert_prices_to_time_format(
        simulations.tolist(), start_time, time_increment
    )

    return predictions