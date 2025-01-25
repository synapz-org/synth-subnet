import numpy as np
import requests
from scipy import stats

def get_asset_price(asset="BTC"):
    """
    Retrieves the current price of the specified asset.
    Currently, supports BTC via Pyth Network.

    Returns:
        float: Current asset price.
    """
    if asset == "BTC":
        btc_price_id = (
            "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43"
        )
        endpoint = f"https://hermes.pyth.network/api/latest_price_feeds?ids[]={btc_price_id}"
        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            data = response.json()
            if not data or len(data) == 0:
                raise ValueError("No price data received")
            price_feed = data[0]
            price = float(price_feed["price"]["price"]) / (10**8)
            return price
        except Exception as e:
            print(f"Error fetching {asset} price: {str(e)}")
            return None
    else:
        print(f"Asset '{asset}' not supported.")
        return None

def simulate_single_price_path(
    current_price, time_increment, time_length, sigma=0.10
):
    one_hour = 3600
    dt = time_increment / one_hour
    num_steps = int(time_length / time_increment)
    
    # Scaled volatility
    daily_vol = sigma * np.sqrt(dt)
    hourly_vol = daily_vol * 0.5
    five_min_vol = hourly_vol * 0.3
    
    # Generate base returns
    base_momentum = stats.t.rvs(df=4.0) * 0.03
    daily_ret = stats.t.rvs(df=4.0) * daily_vol + base_momentum
    
    # Calculate exact number of hours needed
    num_hours = (num_steps + 11) // 12  # Ceiling division by 12
    hourly_rets = stats.t.rvs(df=4.0, size=num_hours) * hourly_vol + base_momentum * 0.4
    five_min_rets = stats.t.rvs(df=4.0, size=num_steps) * five_min_vol + base_momentum * 0.2
    
    # Combine returns
    combined_rets = (0.6 * five_min_rets + 
                    0.3 * np.repeat(hourly_rets, 12)[:num_steps] + 
                    0.1 * daily_ret)
    
    cumulative_returns = np.cumprod(1 + combined_rets)
    cumulative_returns = np.insert(cumulative_returns, 0, 1.0)
    price_path = current_price * cumulative_returns
    return price_path

def simulate_crypto_price_paths(
    current_price, time_increment, time_length, num_simulations, sigma
):
    """
    Simulate multiple crypto asset price paths.
    """
    price_paths = []
    for _ in range(num_simulations):
        price_path = simulate_single_price_path(
            current_price, time_increment, time_length, sigma
        )
        price_paths.append(price_path)
    return np.array(price_paths)