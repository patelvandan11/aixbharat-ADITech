import json
from pydantic import BaseModel, Field, ValidationError
from openai import OpenAI
from app.core.prompts import CONFIDENCE_PROMPT

client = OpenAI()


class ConfidenceResult(BaseModel):
    score: float = Field(..., ge=0.0, le=1.0)
    reason: str


def evaluate_confidence(
    question: str,
    retrieved_context: str
) -> ConfidenceResult:
    """
    Uses LLM to evaluate how well the retrieved context answers the question.
    """

    prompt = CONFIDENCE_PROMPT.format(
        question=question,
        context=retrieved_context
    ) + "\n\nReturn the result strictly as valid JSON."

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a strict JSON generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0
    )

    raw_output = response.choices[0].message.content.strip()

    try:
        parsed = json.loads(raw_output)
        return ConfidenceResult(**parsed)

    except (json.JSONDecodeError, ValidationError):
        # Fallback: assume low confidence
        return ConfidenceResult(
            score=0.0,
            reason="Failed to parse confidence evaluation output."
        )
