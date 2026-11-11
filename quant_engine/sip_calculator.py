import pandas as pd
import numpy as np

class VectorizedSIPSimulator:
    
    def __init__(self, market_data_path: str = "data/historical_nav.csv"):
        self.market_df = pd.read_csv(market_data_path, parse_dates=["date"])
        self.market_df.set_index("date", inplace=True)

    def simulate(self, asset_name: str, monthly_amount: float = 5000.0) -> pd.DataFrame:
        print(f"⚙️ Running Vectorized SIP Simulation for {asset_name} | Amount: ₹{monthly_amount}/month")

        
        monthly_data = self.market_df.resample("BMS").first()
        
        sip_df = pd.DataFrame(index=monthly_data.index)
        sip_df["nav"] = monthly_data[f"{asset_name}_nav"]
        sip_df["sip_amount"] = monthly_amount
        
        sip_df["units_bought"] = sip_df["sip_amount"] / sip_df["nav"]
        
        sip_df["total_units"] = sip_df["units_bought"].cumsum()
        
        sip_df["total_invested"] = sip_df["sip_amount"].cumsum()
        
        sip_df["portfolio_value"] = sip_df["total_units"] * sip_df["nav"]
        
        # Absolute Return (ROI %)
        sip_df["roi_percentage"] = ((sip_df["portfolio_value"] - sip_df["total_invested"]) / sip_df["total_invested"]) * 100
        
        # Rounding for clean output
        return sip_df.round(2).dropna()

# Quick Testing block
if __name__ == "__main__":
    simulator = VectorizedSIPSimulator()
    # Nifty 50 par 5000 ki SIP test karte hain
    results = simulator.simulate(asset_name="nifty_50", monthly_amount=5000)
    print("\n📊 First 5 Months of SIP:")
    print(results.head())
    print("\n💰 Final Portfolio State (After 10 Years):")
    print(results.tail(1)[["total_invested", "portfolio_value", "roi_percentage"]])