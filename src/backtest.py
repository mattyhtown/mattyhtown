import pandas as pd
from .strategy import MovingAverageStrategy


def run_backtest(prices: pd.Series, short_window: int = 20, long_window: int = 50) -> pd.Series:
    """Run a simple backtest of the moving average strategy.

    Returns the equity curve as a pandas Series starting at 1.0.
    """
    strategy = MovingAverageStrategy(short_window=short_window, long_window=long_window)
    signals = strategy.generate_signals(prices)
    returns = prices.pct_change().fillna(0.0)
    strategy_returns = returns * signals["positions"].shift().fillna(0.0)
    equity_curve = (1 + strategy_returns).cumprod()
    equity_curve.name = "equity"
    return equity_curve
