from synth.validator.crps_calculation import calculate_crps_for_miner
from synth.miner.price_simulation import simulate_crypto_price_paths, get_asset_price, simulate_single_price_path
import numpy as np

def test_parameter_combinations():
    current_price = get_asset_price("BTC")
    time_increment = 300
    time_length = 86400
    num_simulations = 100
    
    sigmas = [0.1, 0.3, 0.5]
    alphas = [0.05, 0.1, 0.15]
    betas = [0.8, 0.85, 0.9]
    
    best_score = float('inf')
    best_params = None
    
    for sigma in sigmas:
        for alpha in alphas:
            for beta in betas:
                predictions = simulate_crypto_price_paths(current_price, time_increment, time_length, num_simulations, sigma)
                real_price_path = simulate_single_price_path(current_price, time_increment, time_length, sigma)
                score, _ = calculate_crps_for_miner(predictions, real_price_path, time_increment)
                
                if score < best_score:
                    best_score = score
                    best_params = (sigma, alpha, beta)
                print(f"σ={sigma:.2f}, α={alpha:.2f}, β={beta:.2f} -> CRPS={score:.2f}")
    
    print(f"\nBest parameters: σ={best_params[0]:.2f}, α={best_params[1]:.2f}, β={best_params[2]:.2f}")
    print(f"Best CRPS score: {best_score:.2f}")

if __name__ == "__main__":
    test_parameter_combinations()
