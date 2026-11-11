import pandas as pd
import numpy as np
import os

def generate_market_data(file_path: str = "data/historical_nav.csv", years: int = 10):
    print("📈 Generating Synthetic Market Data (Geometric Brownian Motion)...")
    
    np.random.seed(42)
    
    total_days = years * 252
    dates = pd.date_range(start="2014-01-01", periods=total_days, freq="B")
    
    assets = {
        "nifty_50": {"mu": 0.12, "sigma": 0.15, "start_nav": 100.0},      # 12% return, 15% risk
        "midcap_150": {"mu": 0.15, "sigma": 0.20, "start_nav": 100.0},    # 15% return, 20% risk
        "smallcap_250": {"mu": 0.18, "sigma": 0.25, "start_nav": 100.0},  # 18% return, 25% risk
    }
    
    df = pd.DataFrame({"date": dates})
    dt = 1 / 252  # Time step in years
    
    for name, params in assets.items():
        # Pure NumPy Vectorized GBM Simulation
        drift = (params["mu"] - 0.5 * params["sigma"]**2) * dt
        shock = params["sigma"] * np.sqrt(dt) * np.random.normal(size=total_days)
        daily_returns = np.exp(drift + shock)
        
        # Cumulative product to get NAVs
        navs = params["start_nav"] * np.cumprod(daily_returns)
        df[f"{name}_nav"] = np.round(navs, 4)
        

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"✅ Market data generated with {len(df)} trading days at: {file_path}")

if __name__ == "__main__":
    generate_market_data()