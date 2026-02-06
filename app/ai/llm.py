from openai import OpenAI
from app.core.config import OPENAI_CHAT_MODEL
from app.core.prompts import (
    SYSTEM_PROMPT,
    PDF_ANSWER_PROMPT,
    WIKIPEDIA_ANSWER_PROMPT
)

client = OpenAI()

def generate_answer(
    question: str,
    context: str,
    source: str
) -> str:
    """
    Generates a final answer using the LLM.

    Args:
        question: User's question
        context: Retrieved context (PDF chunks or Wikipedia summary)
        source: 'government_pdf' or 'wikipedia'
    """

    if source == "government_pdf":
        user_prompt = PDF_ANSWER_PROMPT.format(
            question=question,
            context=context
        )

    elif source == "wikipedia":
        user_prompt = WIKIPEDIA_ANSWER_PROMPT.format(
            question=question,
            context=context
        )

    else:
        raise ValueError("Invalid source type")

    response = client.chat.completions.create(
        model=OPENAI_CHAT_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()