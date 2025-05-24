import pandas as pd


def load_prices(csv_path: str) -> pd.Series:
    """Load price data from a CSV file.

    The CSV is expected to have a datetime index in the first column and a
    'Close' column with price data.
    """
    df = pd.read_csv(csv_path, index_col=0, parse_dates=True)
    if 'Close' not in df.columns:
        raise ValueError("CSV must contain a 'Close' column")
    return df['Close']
