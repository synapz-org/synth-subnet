from synth.validator.crps_calculation import calculate_crps_for_miner
from synth.miner.price_simulation import simulate_crypto_price_paths, get_asset_price, simulate_single_price_path
import numpy as np

def test_fine_tuned_t_distribution():
    current_price = get_asset_price("BTC")
    time_increment = 300
    time_length = 86400
    num_simulations = 100
    
    degrees_freedom = [3.8, 3.9, 4.0, 4.1, 4.2]
    
    for df in degrees_freedom:
        predictions = simulate_crypto_price_paths(current_price, time_increment, time_length, num_simulations, sigma=0.10)
        real_price_path = simulate_single_price_path(current_price, time_increment, time_length, sigma=0.10)
        score, _ = calculate_crps_for_miner(predictions, real_price_path, time_increment)
        print(f"Degrees of freedom={df:.1f} -> CRPS={score:.2f}")

if __name__ == "__main__":
    test_fine_tuned_t_distribution()
