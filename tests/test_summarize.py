import json
import logging

from langchain.evaluation.criteria import LabeledCriteriaEvalChain
from langchain_community.llms import Ollama
from rouge import Rouge

from src.summarize import summarize

logger = logging.getLogger(__name__)

criteria = {
    "accuracy": "The output should meets rogue score of 0.5 for rouge-1, 0.3 for rouge-2, and 0.5 for rouge-l.",
}

text = """
Let's explore the concept of urban gardening, an increasingly popular practice that transforms city landscapes and fosters community engagement. Urban gardening involves cultivating plants and vegetables in densely populated urban areas, utilizing rooftops, balconies, vacant lots, and even window sills. This movement not only beautifies the city but also provides fresh produce to residents who might otherwise lack access to green spaces and healthy foods.
The benefits of urban gardening extend beyond aesthetics and nutrition. It promotes environmental responsibility by reducing the urban heat island effect and improving air quality. Green spaces help absorb rainwater, reducing the risk of flooding, and they also sequester carbon, combating urban pollution. Moreover, these gardens create habitats for urban wildlife, supporting biodiversity. Community gardens serve as social hubs where people of diverse backgrounds can connect, share knowledge, and collaborate. They provide educational opportunities for children and adults alike, teaching valuable skills such as composting, planting, and sustainable living. In essence, urban gardening is not just about growing plants—it's about cultivating healthier, more vibrant urban communities. Through these small patches of greenery, city dwellers can reconnect with nature and each other, enhancing the quality of urban life.
"""


def test_summarize_json_format_and_length():
    """
    Test the JSON format, length of the summary, and the title's length.
    """
    json_output = summarize(text)
    data = json.loads(json_output)

    assert "title" in data, "JSON must include a title key."
    assert "summary" in data, "JSON must include a summary key."
    assert len(data["summary"]) <= 100, "Summary must not exceed 100 characters."
    assert len(data["title"]) < len(
        data["summary"]
    ), "Title must be shorter than the summary."


def test_summarize_langchain():
    """
    Test the accuracy of the summarization output using Ollama verifier.
    """
    json_output = summarize(text)
    data = json.loads(json_output)
    summary = data["summary"]

    llm_verifier = Ollama(model="llama3")
    evaluator = LabeledCriteriaEvalChain.from_llm(llm=llm_verifier, criteria=criteria)
    result = evaluator.evaluate_strings(
        prediction=summary,
        reference=text,
        input=text,  # Adjusted to use 'text' instead of 'prompt'
    )
    logger.info("result_relevance: %s", result)
    assert result["score"] == 1, result


def test_summarize_rouge(reference_model):
    """
    Test the summarization output against a reference model using ROUGE scores.
    """
    json_output = summarize(text)
    data = json.loads(json_output)
    summary = data["summary"]

    reference_summary = reference_model(
        text, max_length=50, min_length=50, do_sample=False
    )[0]["summary_text"]

    rouge = Rouge()
    scores = rouge.get_scores(summary, reference_summary)

    assert scores[0]["rouge-1"]["f"] > 0.5, "ROUGE-1 F1 score should be above 0.5"
    assert scores[0]["rouge-2"]["f"] > 0.3, "ROUGE-2 F1 score should be above 0.3"
    assert scores[0]["rouge-l"]["f"] > 0.5, "ROUGE-L F1 score should be above 0.5"
