import random

import pytest
from datasets import load_dataset

from src.sentiment import analyze_sentiment

CONFIDENCE_THRESHOLD = 0.8
NUM_TESTS = 10
dataset = load_dataset("go_emotions", "simplified", split="train")
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
        ("I love this product!", "love"),
        ("This movie is terrible", "negative"),
        ("", "neutral"),
        ("Happy with the results of this tool.", "happy"),
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


@pytest.mark.parametrize(
    "sample",
    [dataset[random.randint(0, len(dataset) - 1)] for _ in range(NUM_TESTS)],
)
def test_analyze_sentiment_dataset(sample):
    """
    Test analyze_sentiment function with dataset
    """
    text = sample["text"]
    expected_emotions = [
        label_to_emotion[label] for _, label in enumerate(sample["labels"])
    ]

    result = analyze_sentiment(text)
    emotion = next(iter(result))

    # Check that the returned label is expected
    assert (
        emotion in expected_emotions
    ), f"Expected emotions: {expected_emotions}, but got: {result}"
