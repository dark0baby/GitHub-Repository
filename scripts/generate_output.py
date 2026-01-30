import json
import os
from datetime import datetime
from fetch_news import fetch_news
from analyze_market import analyze

DATA_DIR = "data"

def save_data(records):
    os.makedirs(DATA_DIR, exist_ok=True)
    today = datetime.utcnow().strftime("%Y-%m-%d")
    daily_file = f"{DATA_DIR}/{today}.json"

    with open(daily_file, "w") as f:
        json.dump(records, f, indent=2)

    all_file = f"{DATA_DIR}/all_news.json"
    if os.path.exists(all_file):
        with open(all_file) as f:
            existing = json.load(f)
    else:
        existing = []

    existing.extend(records)

    with open(all_file, "w") as f:
        json.dump(existing, f, indent=2)

if __name__ == "__main__":
    raw_news = fetch_news()
    analyzed = analyze(raw_news)
    save_data(analyzed)
