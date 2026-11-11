import pandas as pd
import numpy as np

class RiskAnalyzer:
    """
    Computes advanced portfolio risk metrics using vectorized Pandas operations.
    """
    
    @staticmethod
    def calculate_drawdown(portfolio_series: pd.Series) -> pd.DataFrame:
        """
        Calculates how much the portfolio has dropped from its all-time high.
        """
        # 1. Har point tak ka All-Time High nikalna (Vectorized)
        rolling_max = portfolio_series.cummax()
        
        # 2. Drawdown formula: (Current - Peak) / Peak
        drawdown = (portfolio_series - rolling_max) / rolling_max
        
        dd_df = pd.DataFrame({
            "portfolio_value": portfolio_series,
            "peak_value": rolling_max,
            "drawdown_pct": drawdown * 100
        })
        
        return dd_df.round(2)

    @staticmethod
    def get_risk_summary(sip_df: pd.DataFrame) -> dict:
        """Generates a clean summary dictionary of portfolio performance."""
        final_row = sip_df.iloc[-1]
        
        # Drawdown calculate karo
        dd_df = RiskAnalyzer.calculate_drawdown(sip_df["portfolio_value"])
        max_dd = dd_df["drawdown_pct"].min() # Sabse negative value
        
        summary = {
            "Total Invested (₹)": float(final_row["total_invested"]),
            "Final Portfolio Value (₹)": float(final_row["portfolio_value"]),
            "Absolute ROI (%)": float(final_row["roi_percentage"]),
            "Maximum Drawdown (%)": float(max_dd)
        }
        return summary

# Quick Testing
if __name__ == "__main__":
    from sip_calculator import VectorizedSIPSimulator
    
    simulator = VectorizedSIPSimulator("data/historical_nav.csv")
    sip_data = simulator.simulate("nifty_50", 5000)
    
    analyzer = RiskAnalyzer()
    summary = analyzer.get_risk_summary(sip_data)
    
    print("\n📉 PORTFOLIO RISK SUMMARY:")
    for key, value in summary.items():
        print(f"  • {key}: {value}") 