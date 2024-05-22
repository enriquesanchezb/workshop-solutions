import logging
from enum import Enum

from transformers import pipeline


class Model(Enum):
    ROBERTA = "SamLowe/roberta-base-go_emotions"


def analyze_sentiment_with_model(text: str, model_enum: Model) -> dict:
    """
    Analyze sentiment of text using a specified model.
    Returns a dictionary of sentiment scores.
    """
    try:
        sentiment_pipeline = pipeline(
            task="text-classification", model=model_enum.value
        )
        results = sentiment_pipeline(text)

        # Different handling depending on the model
        if model_enum == Model.ROBERTA:
            sentiment_results = {result["label"]: result["score"] for result in results}
            return sentiment_results

    except Exception as e:
        logging.error(
            "Error processing sentiment analysis for %s: %s", model_enum.name, str(e)
        )
    else:
        return {}


def analyze_sentiment(text: str, model: Model = Model.ROBERTA) -> dict:
    """Wrapper function to analyze sentiment, defaults to ROBERTA model."""
    return analyze_sentiment_with_model(text, model)
