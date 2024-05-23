import logging

from langchain.evaluation.criteria import LabeledCriteriaEvalChain
from langchain_community.llms import Ollama

from src.shakespearean import shakespearean

logger = logging.getLogger(__name__)


def test_shakespeare_langchain():
    """
    Test the accuracy of the summarization output using Ollama verifier.
    """
    text = "The quick brown fox jumps over the lazy dog."
    criteria = {
        "accuracy": "The output should be a Shakespearean translation of the input text.",
    }
    data = shakespearean(text)

    llm_verifier = Ollama(model="llama3")
    evaluator = LabeledCriteriaEvalChain.from_llm(llm=llm_verifier, criteria=criteria)
    result = evaluator.evaluate_strings(
        prediction=data,
        reference=text,
        input=text,  # Adjusted to use 'text' instead of 'prompt'
    )
    logger.info("result_relevance: %s", result)
    assert result["score"] == 1, result
