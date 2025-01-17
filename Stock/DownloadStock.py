import yfinance as yf
from datetime import datetime, timedelta

# Calculate today's date and one year ago
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')

# Function to fetch stock data
def fetch_stock_data(ticker):
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        

        if data.empty:
            raise ValueError(f"No data found for {ticker}")

        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

# Fetch data for TCS.NS
stock = fetch_stock_data('TCS.NS')
# get list of news


if stock is not None:
    print(stock.head())
    print(yf.Search("TCS.NS", news_count=3).news)
else:
    print("TCS.NS data could not be retrieved.")
