
Yahoo Finance provides stock-related news, including articles, press releases, and financial updates. While the yfinance Python library is primarily for fetching historical and real-time stock data, it does not directly support fetching news. For accessing Yahoo Finance news about a specific stock, you can scrape the Yahoo Finance website or use APIs like RapidAPI Yahoo Finance

Below are methods to fetch stock news:

1. Using yahoo_fin Library (News Fetching) The yahoo_fin library provides a straightforward way to fetch stock-related news.

Install the Library: pip install yahoo_fin
1. Using RapidAPI Yahoo Finance API

Steps:
Create a RapidAPI account.
Subscribe to the Yahoo Finance API.
Fetch stock news via the API.

import requests

url = "https://yh-finance.p.rapidapi.com/news/v2/list"
querystring = {"region": "US", "snippetCount": "10"}
headers = {
    "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",
    "X-RapidAPI-Host": "yh-finance.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
news_data = response.json()

# Extract and display news
for item in news_data['data']['main']['stream']:
    title = item.get('title', 'No title available')
    link = item.get('link', 'No link available')
    print(f"Title: {title}")
    print(f"Link: {link}")
    print()

3. Scraping Yahoo Finance Website
Use the BeautifulSoup library to scrape stock news directly from Yahoo Finance.

Install Libraries:
bash
Copy
Edit
pip install requests beautifulsoup4
Code Example:
python
Copy
Edit
import requests
from bs4 import BeautifulSoup

# Yahoo Finance URL for stock news
ticker = "AAPL"
url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}"

# Fetch and parse the webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract news headlines
news_section = soup.find_all('h3', class_='Mb(5px)')  # News headline class
for news in news_section:
    title = news.get_text()
    link = news.find('a')['href']
    print(f"Title: {title}")
    print(f"Link: https://finance.yahoo.com{link}")
    print()
