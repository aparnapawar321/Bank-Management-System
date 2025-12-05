import download_data as yf
import pandas as pd
import os

# List of symbols to download (NSE symbols on Yahoo Finance usually end with ".NS")
symbols = [
    "RELIANCE.NS",
    "TCS.NS",
    "HDFCBANK.NS",
    "INFY.NS",
    "ICICIBANK.NS"
]

# Create data folder if it doesn't exist
os.makedirs("./data", exist_ok=True)

for symbol in symbols:
    print(f"Downloading data for {symbol}...")
    # Get last 1 year of daily data (more than 250 trading days)
    df = yf.download(symbol, period="1y", interval="1d")

    # Keep only required columns and rename to match your scan logic
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']].rename(
        columns={'Open':'open', 'High':'high', 'Low':'low', 'Close':'close', 'Volume':'volume'}
    )

    # Reset index to have 'date' column
    df.reset_index(inplace=True)
    df['date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df = df[['date','open','high','low','close','volume']]

    # Save to CSV in ./data folder
    csv_path = "./data.csv"
    df.to_csv(csv_path, index=False)
    print(f"Saved {csv_path}, rows: {len(df)}")

print("Download complete!")
