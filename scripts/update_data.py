#!/usr/bin/env python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from config.settings import DATA_DIR, SYMBOLS

def get_last_date(symbol):
    filepath = DATA_DIR / f"{symbol}.parquet"
    if filepath.exists():
        df = pd.read_parquet(filepath)
        if not df.empty:
            return df.index.max()
    return None

def download_symbol(symbol, start, end):
    print(f"Downloading {symbol} from {start.date()} to {end.date()}")
    data = yf.download(symbol, start=start, end=end, progress=False)
    if data.empty:
        return pd.DataFrame()
    data.index = pd.to_datetime(data.index)
    return data

def update_data(symbol):
    end = datetime.today()
    last = get_last_date(symbol)
    start = (last + timedelta(days=1)) if last else datetime(2000, 1, 1)
    if start <= end:
        new = download_symbol(symbol, start, end)
        if not new.empty:
            filepath = DATA_DIR / f"{symbol}.parquet"
            if filepath.exists():
                old = pd.read_parquet(filepath)
                combined = pd.concat([old, new])
                combined = combined[~combined.index.duplicated(keep='last')].sort_index()
            else:
                combined = new
            combined.to_parquet(filepath)
            print(f"Updated {symbol}: {len(new)} new rows")
        else:
            print(f"No new data for {symbol}")
    else:
        print(f"No new data for {symbol}")

def main():
    for symbol in SYMBOLS:
        update_data(symbol)
    print("All symbols updated.")

if __name__ == "__main__":
    main()
