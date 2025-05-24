# Quant Trading Strategy Environment

**Disclaimer:** this is not financial advice.

This repository provides a starting point for developing algorithmic trading strategies in Python. It includes a basic moving average crossover strategy, simple data loading utilities, and a backtesting helper along with pytest tests.

## Requirements

- Python 3.8+
- See `requirements.txt` for Python package dependencies.

## Setup

1. Create and activate a virtual environment (optional).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run tests:

```bash
pytest
```

## Project Structure

- `src/` – Source code for strategies, data loaders, and backtesting utilities.
- `tests/` – Pytest test suite.
- `LICENSE` – MIT license information.

## Usage Example

Load price data and run a simple backtest:

```python
from src import load_prices, run_backtest

prices = load_prices("prices.csv")
equity = run_backtest(prices, short_window=20, long_window=50)
print(equity.tail())
```

## Next Steps

Expand the strategies, add more robust data loaders, backtesting features, and analytics as needed.
