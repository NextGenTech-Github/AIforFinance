from yahoo_fin import news

# Fetch news for a specific stock
ticker = "TCS.NS"  # Example: Apple
news_data = news.get_yf_rss(ticker)
#print(news_data)
#rint(news_data.get('summary','No summary found'))

print(f"Summary:")
for summary in news_data: 
    title = summary.get('title', 'No title available')
    pub_date = summary.get('published','Not Avaliable')
    print(f"Title: {title} : {pub_date}")

# Display news
print(f"Article:")
for article in news_data:
    
    title = article.get('title', 'No title available')
    link = article.get('link', 'No link available')
    pub_date = article.get('published', 'Not Available')  # Use a default value if 'pubDate' is missing
    print(f"Title: {title}")
    print(f"Link: {link}")
    print(f"Published Date: {pub_date}")
    print()
