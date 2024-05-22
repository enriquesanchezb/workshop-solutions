import re

from langchain_community.llms import Ollama

from prompt.shakespeare import prompt as shakespearean_template
from src.prompt_helper import execute_prompt, generate_prompt


def clean_response(response):
    # Remove unwanted characters and substrings
    return re.sub(r"```json\n|```", "", response).strip()


def shakespearean(text: str, llm: str = "phi3") -> str:
    """translate a text."""

    llm = Ollama(model=llm)
    system_message_prompt_template = shakespearean_template[
        "systemMessagePromptTemplate"
    ]
    human_prompt_template = shakespearean_template["humanPromptTemplate"]
    prompt = generate_prompt(
        system_message_prompt_template, human_prompt_template, text
    )

    output = execute_prompt(llm, prompt, text)
    output_parser = clean_response(output)
    return output_parser
