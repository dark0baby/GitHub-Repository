def analyze(news):
    analysis = []

    for item in news:
        analysis.append({
            "what": item["title"],
            "when": "Recent",
            "why_it_matters": "Macro or sector-level impact on Indian markets",
            "past_reaction": "Similar events caused volatility",
            "rbi_repo": "Possible pressure on RBI stance",
            "banking": "Short-term impact expected",
            "large_cap": ["HDFC Bank", "ICICI Bank"],
            "mid_cap": ["Federal Bank"],
            "small_cap": [],
            "sectors": ["Banking", "Financials"],
            "confidence": "Medium"
        })

    return analysis
