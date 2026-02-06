from pydantic import BaseModel, Field
from openai import OpenAI
from core.prompts import CONFIDENCE_PROMPT

client = OpenAI()

# ---- Output schema ----
class ConfidenceResult(BaseModel):
    score: float = Field(..., ge=0.0, le=1.0)
    reason: str


# ---- Main function ----
def evaluate_confidence(
    question: str,
    retrieved_context: str
) -> ConfidenceResult:
    """
    Evaluates how well the retrieved context answers the question.
    Returns a confidence score between 0 and 1.
    """

    prompt = CONFIDENCE_PROMPT.format(
        question=question,
        context=retrieved_context
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        response_format=ConfidenceResult
    )

    return response.output_parsed
