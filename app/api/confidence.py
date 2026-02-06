from pydantic import BaseModel, Field
from openai import OpenAI
from app.ai.confidence import ConfidenceScore
from dotenv import load_dotenv

class ConfidenceScore(BaseModel):
    score: float = Field(..., ge=0.0, le=1.0)
    reason: str

client = OpenAI()

def evaluate_confidence(query: str, context: str) -> ConfidenceScore:
    prompt = f"""
You are an evaluator.

Given a user question and retrieved information, rate how well the information answers the question.

Return a JSON object with:
- score: float between 0 and 1
- reason: short explanation

Question:
{query}

Retrieved Information:
{context}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        response_format=ConfidenceScore
    )

    return response.output_parsed
