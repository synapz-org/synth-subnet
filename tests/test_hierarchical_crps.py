from synth.validator.crps_calculation import calculate_crps_for_miner
from synth.miner.price_simulation import get_asset_price, simulate_crypto_price_paths, simulate_single_price_path
import numpy as np

def test_hierarchical_sampling():
    current_price = get_asset_price("BTC")
    time_increment = 300  # 5 minutes
    time_length = 86400  # 24 hours
    num_simulations = 100
    sigma = 0.10
    
    # Test across multiple timeframes
    timeframes = [300, 1800, 10800, 86400]  # 5min, 30min, 3hr, 24hr
    
    for tf in timeframes:
        predictions = simulate_crypto_price_paths(current_price, time_increment, tf, num_simulations, sigma)
        real_price_path = simulate_single_price_path(current_price, time_increment, tf, sigma)
        score, _ = calculate_crps_for_miner(predictions, real_price_path, time_increment)
        print(f"Timeframe={tf/60:.0f}min -> CRPS={score:.2f}")

if __name__ == "__main__":
    test_hierarchical_sampling()
