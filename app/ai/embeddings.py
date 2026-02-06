from openai import OpenAI
from app.core.config import OPENAI_EMBEDDING_MODEL

client = OpenAI()

def generate_embedding(text: str) -> list[float]:
    """
    Converts a text chunk into a vector embedding.

    Args:
        text: Clean text chunk from PDF or query

    Returns:
        List of floats (embedding vector)
    """

    response = client.embeddings.create(
        model=OPENAI_EMBEDDING_MODEL,
        input=text
    )

    return response.data[0].embedding
