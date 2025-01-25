from synth.miner.simulations import generate_simulations
from synth.validator.crps_calculation import calculate_crps_for_miner
from synth.miner.price_simulation import get_asset_price
import numpy as np
from datetime import datetime
def test_enhanced_predictions():
    start_time = datetime.now().isoformat()
    timeframes = [300, 1800, 10800, 86400]  # 5min, 30min, 3hr, 24hr
    current_price = get_asset_price("BTC")
    
    for tf in timeframes:
        predictions_dict = generate_simulations(
            start_time=start_time,
            time_increment=300,
            time_length=tf,
            num_simulations=100
        )
        # Extract price values from predictions
        predictions = np.array([[p['price'] for p in path] for path in predictions_dict])
        real_path = np.array([current_price] * (tf//300 + 1))
        score, _ = calculate_crps_for_miner(predictions, real_path, 300)
        print(f"Timeframe={tf/60:.0f}min -> CRPS={score:.2f}")
if __name__ == "__main__":
    test_enhanced_predictions()
