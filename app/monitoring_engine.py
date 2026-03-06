import random


def analyze_response(text: str):
    confidence_score = round(random.uniform(0.6, 0.95), 2)

    sentiment = "positive" if "good" in text.lower() else "neutral"

    return {
        "confidence_score": confidence_score,
        "sentiment": sentiment
    }