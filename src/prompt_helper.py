"""Module for prompt execution."""

from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.language_models import BaseLanguageModel


def clean_spaces(text: str) -> str:
    """Cleans spaces from a text."""
    return text.strip().replace("\n", "")


def generate_prompt(
    system_message_prompt_template: str,
    human_prompt_template: str,
    text_to_replace: str,
) -> str:
    """Generates a prompt using the given templates."""

    system_message_prompt = SystemMessagePromptTemplate.from_template(
        system_message_prompt_template
    )
    human_message_prompt = HumanMessagePromptTemplate.from_template(
        human_prompt_template
    )
    prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    formatted_prompt = prompt.format_messages(
        text=clean_spaces(text_to_replace),
    )
    return formatted_prompt


def execute_prompt(
    llm: BaseLanguageModel,
    prompt: str,
    text_to_replace: str,
) -> str:
    """Evaluates a prompt using a given model and prompt templates."""

    prompt = ChatPromptTemplate.from_messages(prompt)
    chain = prompt | llm

    result = chain.invoke({"text": text_to_replace})
    return result
