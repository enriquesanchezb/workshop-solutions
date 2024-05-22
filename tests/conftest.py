import pytest
from transformers import pipeline


@pytest.fixture(scope="module")
def reference_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")
