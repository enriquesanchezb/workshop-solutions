import random

import pytest
from datasets import load_dataset

from src.sentiment import analyze_sentiment

CONFIDENCE_THRESHOLD = 0.8
NUM_TESTS = 10

label_to_emotion = {
    0: "admiration",
    1: "amusement",
    2: "anger",
    3: "annoyance",
    4: "approval",
    5: "caring",
    6: "confusion",
    7: "curiosity",
    8: "desire",
    9: "disappointment",
    10: "disapproval",
    11: "disgust",
    12: "embarrassment",
    13: "excitement",
    14: "fear",
    15: "gratitude",
    16: "grief",
    17: "joy",
    18: "love",
    19: "nervousness",
    20: "optimism",
    21: "pride",
    22: "realization",
    23: "relief",
    24: "remorse",
    25: "sadness",
    26: "surprise",
    27: "neutral",
}


@pytest.mark.parametrize(
    "text, expected_result",
    [
        ("love", "love"),
        ("what a surprise", "surprise"),
        ("", "neutral"),
        ("test test test asdf", "neutral"),
    ],
)
def test_analyze_sentiment(text, expected_result):
    """
    Test analyze_sentiment function
    """
    result = analyze_sentiment(text)

    assert expected_result in result, f"Expected: {expected_result}, Actual: {result}"
    assert (
        result[expected_result] > CONFIDENCE_THRESHOLD
    ), f"Confidence: {result[expected_result]}"


def test_analyze_sentiment_dataset():
    """
    Test analyze_sentiment function with dataset
    """
    dataset = load_dataset("go_emotions", "simplified", split="train")
    sample = [dataset[random.randint(0, len(dataset) - 1)] for _ in range(NUM_TESTS)]
    total = 0
    for s in sample:
        text = s["text"]
        expected_emotions = [
            label_to_emotion[label] for _, label in enumerate(s["labels"])
        ]

        result = analyze_sentiment(text)
        emotion = next(iter(result))
        if emotion in expected_emotions:
            total += 1
    assert total >= NUM_TESTS * 0.5
