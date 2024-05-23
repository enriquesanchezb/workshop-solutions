# Branch: 4-Summarization

Welcome to the 4-summarization branch of our AI Testing workshop! In this section, you will tackle the challenge of summarizing text and testing the effectiveness of those summaries under various scenarios.

## Installation

Follow the same installation steps as in the previous exercises:

```
poetry install
```
 
## Running the Tests

To run the tests, you can run

```bash
poetry install
poetry run pytest tests/test_summarize.py
poetry run pytest tests/test_security.py
poetry run pytest tests
```

## Understanding the Challenge

Testing automatic text summarization introduces unique challenges, as the output can vary with each run. This makes it difficult to predict and verify the accuracy of the summary programmatically. You'll need to consider these variations when designing your tests.

## Exercises

### Exercise 1

In this exercise, we will modify the prompt to ensure it adheres to the following specifications:

- The response should be a JSON object with two fields: title and summary.
- The summary must be less than 100 characters in length.
- The title must always be shorter than the summary.
- The response should be concise.

**Instructions**

- Modify the prompt template to include the specified constraints.
- Write test cases to validate the requirements.

### Exercise 2

Let's create a new feature: translate the text into Latin. Follow these specifications:

- The response should be a JSON object with two fields: originalText and translation.

**Instructions**

- Add the new feature as code.
- Write tests cases to validate the requirements.

### Exercise 3

From the original text, convert it to a Shakespearean tone, using archaic expressions while maintaining the original meaning of the text.

- The response should be a str

**Instructions**

- Add the new feature as code.
- Write tests cases to validate the requirements.

### Exercise 4

Take a look into the security tests and try to fix the prompt to avoid the issues. Create more tests to ensure the system is secure.


## Tips for Testing

The best way to do verifications is using libraries for evaluation. Some libraries you can use are:
- [Langchain Evaluators](https://python.langchain.com/v0.1/docs/guides/productionization/evaluation/). For this case you can use [criteria evaluation](https://python.langchain.com/v0.1/docs/guides/productionization/evaluation/string/criteria_eval_chain/).
- [ROUGE](https://en.wikipedia.org/wiki/ROUGE_(metric)). You can use the Python implementation [rouge](https://pypi.org/project/rouge/)

For security you can take a look about [OWASP recommendations](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

## Support

For any questions or issues you encounter, please reach out to the workshop organizers.

---

Explore the complexities of AI-driven text summarization and enhance your testing strategies!

---