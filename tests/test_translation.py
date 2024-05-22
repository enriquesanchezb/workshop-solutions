import json

from src.translation import translate


def test_translation():
    """
    Ensure the translation follows the expected JSON format.
    """
    text = "Knowledge is power."
    translation = translate(text)
    # Assuming the translation function returns JSON formatted string
    data = json.loads(translation)

    assert "translation" in data, "The output JSON must contain a 'translation' key."
    assert "originalText" in data, "The output JSON must contain an 'originalText' key."
    assert (
        data["originalText"] == text
    ), "The original text should match the input text."
    assert (
        data["translation"] == "Scientia potentia est."
    ), "The translation is incorrect."
