from synth.validator.crps_calculation import calculate_crps_for_miner
from synth.miner.price_simulation import simulate_crypto_price_paths, get_asset_price, simulate_single_price_path
import numpy as np

def test_garch_crps():
    current_price = get_asset_price("BTC")
    time_increment = 300  # 5 minutes
    time_length = 86400  # 24 hours
    num_simulations = 100
    sigma = 0.5
    
    predictions = simulate_crypto_price_paths(current_price, time_increment, time_length, num_simulations, sigma)
    real_price_path = simulate_single_price_path(current_price, time_increment, time_length, sigma)
    
    score, _ = calculate_crps_for_miner(predictions, real_price_path, time_increment)
    print(f"CRPS Score: {score}")
    return score

if __name__ == "__main__":
    test_garch_crps()
