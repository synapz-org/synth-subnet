from synth.miner.price_simulation import get_asset_price, simulate_crypto_price_paths
import matplotlib.pyplot as plt
import numpy as np

# Get current BTC price
current_price = get_asset_price("BTC")

# Simulation parameters
time_increment = 300  # 5 minutes in seconds
time_length = 86400  # 24 hours in seconds
num_simulations = 100
sigma = 0.5  # Volatility parameter

# Generate price paths
paths = simulate_crypto_price_paths(current_price, time_increment, time_length, num_simulations, sigma)

# Plot results
plt.figure(figsize=(12, 6))
for path in paths:
    plt.plot(path, alpha=0.1, color='blue')
plt.plot(paths.mean(axis=0), color='red', linewidth=2, label='Mean Path')
plt.title(f'BTC Price Simulations\nStarting Price: ${current_price:,.2f}')
plt.ylabel('Price ($)')
plt.xlabel('5-minute Intervals')
plt.legend()
plt.savefig('price_simulations.png')
plt.close()
