import pandas as pd

class MovingAverageStrategy:
    """Simple moving average crossover strategy."""

    def __init__(self, short_window: int = 20, long_window: int = 50):
        if short_window <= 0 or long_window <= 0:
            raise ValueError("Window lengths must be positive")
        if short_window >= long_window:
            raise ValueError("Short window must be less than long window")
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, prices: pd.Series) -> pd.DataFrame:
        """Generate trading signals."""
        signals = pd.DataFrame(index=prices.index)
        signals["price"] = prices
        signals["short_ma"] = prices.rolling(window=self.short_window).mean()
        signals["long_ma"] = prices.rolling(window=self.long_window).mean()
        signals["signal"] = 0.0
        signals.loc[self.short_window:, "signal"] = (
            signals.loc[self.short_window:, "short_ma"]
            > signals.loc[self.short_window:, "long_ma"]
        ).astype(float)
        signals["positions"] = signals["signal"].diff().fillna(0.0)
        return signals
