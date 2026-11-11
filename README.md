
# 📈 Quant Analytics: Vectorized SIP & Risk Simulator

> A high-performance quantitative finance engine simulating Systematic Investment Plans (SIP) and portfolio risk metrics using pure Pandas/NumPy vectorization (zero `for` loops).

[![Python 3.12+](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![Managed with uv](<https://img.shields.io/badge/managed%20by-uv-DE5FE9.svg>)](https://github.com/astral-sh/uv)
[![Domain](<https://img.shields.io/badge/Domain-Quantitative%20Finance-success.svg>)]()

---

## 📌 Problem Statement

Many financial analysts and early data scientists calculate portfolio returns over time-series data using `.iterrows()` or native Python `for` loops. This approach is computationally expensive and scales poorly with large tick-level datasets.

**Vectorized Quant Simulator** solves this by:

1. Simulating 10 years of market data using the **Geometric Brownian Motion (GBM)** stochastic model.
2. Calculating monthly SIP unit allocations, cumulative investments, and portfolio valuations in milliseconds using `pandas.Series.cumsum()`.
3. Computing advanced risk metrics (like Maximum Drawdown) using `cummax()` vectorized rolling aggregations.

---

## 🏗️ Architecture

```text
Market Data Generator (GBM Model)
        │ (NumPy Random Normal, Volatility Drift)
        ▼
data/historical_nav.csv (Daily NAVs)
        │
        ▼
VectorizedSIPSimulator (Core Engine)
        │ (Resampling to Business Month Start 'BMS')
        ├──> Vectorized Unit Allocation (Amount / NAV)
        └──> Cumulative Sums for Total Investment & Portfolio Value
        │
        ▼
RiskAnalyzer
        └──> All-Time High Tracking (cummax)
        └──> Maximum Drawdown % Calculation
        │
        ▼
Terminal Console Report (Multi-Asset Comparison)
```

---

## 📊 10-Year Simulation Results (₹5,000/month)

*Simulated via Geometric Brownian Motion with predefined $\mu$ (Expected Return) and $\sigma$ (Volatility).*

| Asset Class            | Total Invested (₹) | Final Value (₹) | Absolute ROI (%)  | Max Drawdown (%) |
| :--------------------- | :------------------ | :--------------- | :---------------- | :--------------- |
| **NIFTY 50**     | 5,80,000.0          | 18,39,893.21     | **217.22%** | **-8.76%** |
| **MIDCAP 150**   | 5,80,000.0          | 6,72,084.42      | 15.88%            | -25.18%          |
| **SMALLCAP 250** | 5,80,000.0          | 7,03,687.20      | 21.33%            | -25.98%          |

> **Quant Insight:** In this stochastic path simulation, highly volatile assets (Smallcap/Midcap) suffered from *Volatility Drag*, leading to lower absolute returns compared to the stable Nifty 50 index, despite having higher expected mean returns ($\mu$).

---

## 🛠️ Technical Concepts Demonstrated

- **Quantitative Finance:** Geometric Brownian Motion (GBM), Systematic Investment Plans (SIP), Maximum Drawdown.
- **Advanced Pandas Vectorization:** Eliminating iterative loops via `cumsum()`, `cummax()`, and vectorized arithmetic.
- **Time-Series Manipulation:** Resampling daily data to business months (`BMS`) using `pd.DataFrame.resample()`.
- **Reproducibility:** Seed-locked pseudo-random number generation (`np.random.seed(42)`).

---

## 🚀 Quickstart

### Prerequisites

Install [uv](https://github.com/astral-sh/uv):

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Installation & Execution

```bash
# Clone the repository
git clone https://github.com/Prabhat0770/quant-simulator.git

cd quant_simulator

# Sync environment
uv sync

# 1. Generate Synthetic Market Data
uv run data/generate_market_data.py

# 2. Run the Vectorized Backtester
uv run main.py
```
