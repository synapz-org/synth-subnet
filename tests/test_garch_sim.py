from synth.miner.price_simulation import get_asset_price, simulate_crypto_price_paths
import matplotlib.pyplot as plt
import numpy as np

current_price = get_asset_price("BTC")
time_increment = 300  # 5 minutes
time_length = 86400  # 24 hours
num_simulations = 100
sigma = 0.5

paths = simulate_crypto_price_paths(current_price, time_increment, time_length, num_simulations, sigma)

plt.figure(figsize=(15, 8))
plt.subplot(2, 1, 1)
for path in paths:
    returns = np.diff(np.log(path))
    plt.plot(returns, alpha=0.1, color='blue')
plt.title('Returns Volatility Clustering')
plt.ylabel('Log Returns')

plt.subplot(2, 1, 2)
plt.hist([np.diff(np.log(path)).flatten() for path in paths], bins=50, density=True)
plt.title('Returns Distribution')
plt.xlabel('Log Returns')
plt.tight_layout()
plt.savefig('garch_analysis.png')
plt.close()
