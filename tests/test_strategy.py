import pandas as pd
from src.strategy import MovingAverageStrategy


def test_generate_signals_columns():
    prices = pd.Series(range(100))
    strat = MovingAverageStrategy(short_window=5, long_window=10)
    signals = strat.generate_signals(prices)
    assert all(c in signals.columns for c in ["price", "short_ma", "long_ma", "signal", "positions"])


def test_invalid_windows():
    try:
        MovingAverageStrategy(short_window=10, long_window=5)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for invalid window lengths")

from src.backtest import run_backtest
from src.data import load_prices
def test_run_backtest_returns_series():
    prices = pd.Series(range(1, 101))
    equity = run_backtest(prices, short_window=5, long_window=20)
    assert len(equity) == len(prices)
    assert equity.iloc[0] == 1.0


def test_load_prices(tmp_path):
    csv_path = tmp_path / "prices.csv"
    df = pd.DataFrame({"Close": range(10)})
    df.to_csv(csv_path)
    loaded = load_prices(csv_path)
    assert loaded.equals(df["Close"]) 

