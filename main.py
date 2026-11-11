import pandas as pd
from quant_engine.sip_calculator import VectorizedSIPSimulator
from quant_engine.risk_metrics import RiskAnalyzer

def run_backtest():
    print("\n" + "=" * 70)
    print("🚀 QUANT ANALYTICS: VECTORIZED SIP BACKTESTER")
    print("=" * 70)

    data_path = "data/historical_nav.csv"
    try:
        simulator = VectorizedSIPSimulator(data_path)
    except FileNotFoundError:
        print("❌ Data not found! Please run 'uv run data/generate_market_data.py' first.")
        return

    analyzer = RiskAnalyzer()
    assets = ["nifty_50", "midcap_150", "smallcap_250"]
    monthly_investment = 5000

    results = []

    # Run vectorized backtest for all assets
    for asset in assets:
        sip_df = simulator.simulate(asset_name=asset, monthly_amount=monthly_investment)
        summary = analyzer.get_risk_summary(sip_df)
        summary["Asset"] = asset.replace("_", " ").upper()
        results.append(summary)

    # Convert results to a pandas DataFrame for a clean terminal table
    report_df = pd.DataFrame(results)
    
    # Reorder columns for professional display
    cols = ["Asset", "Total Invested (₹)", "Final Portfolio Value (₹)", "Absolute ROI (%)", "Maximum Drawdown (%)"]
    report_df = report_df[cols]
    
    print("\n📊 10-YEAR SIP COMPARISON REPORT (₹5,000/month)")
    print("-" * 80)
    print(report_df.to_string(index=False))
    print("-" * 80 + "\n")

if __name__ == "__main__":
    run_backtest()