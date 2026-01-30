import feedparser
from datetime import datetime

RSS_FEEDS = [
    "https://www.livemint.com/rss/markets",
    "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms",
    "https://www.moneycontrol.com/rss/marketreports.xml"
]

KEYWORDS = [
    "RBI", "repo", "inflation", "GDP", "Fed", "interest rate",
    "bank", "fii", "dii", "crude", "budget", "monetary"
]

def fetch_news():
    news_items = []
    today = datetime.utcnow().strftime("%Y-%m-%d")

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:10]:
            title = entry.title
            summary = entry.get("summary", "")

            if any(k.lower() in title.lower() for k in KEYWORDS):
                news_items.append({
                    "date": today,
                    "title": title,
                    "summary": summary[:400]
                })

    return news_items

if __name__ == "__main__":
    data = fetch_news()
    print(data)
