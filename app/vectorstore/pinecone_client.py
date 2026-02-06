from pinecone import Pinecone, ServerlessSpec
from app.core.config import (
    PINECONE_API_KEY,
    PINECONE_ENV,
    PINECONE_INDEX_NAME
)

# ============================
# Initialize Pinecone Client
# ============================

pc = Pinecone(api_key=PINECONE_API_KEY)


# ============================
# Create / Connect Index
# ============================

def get_index():
    """
    Creates the Pinecone index if it does not exist
    and returns the index instance.
    """

    existing_indexes = [idx.name for idx in pc.list_indexes()]

    if PINECONE_INDEX_NAME not in existing_indexes:
        pc.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region=PINECONE_ENV  # example: "us-east-1"
            )
        )

    return pc.Index(PINECONE_INDEX_NAME)


index = get_index()


# ============================
# Upsert Vectors
# ============================

def upsert_records(records: list[dict]):
    """
    Inserts vectors into Pinecone.

    Each vector:
    {
        "id": str,
        "values": list[float],
        "metadata": dict
    }
    """

    index.upsert(vectors=records)


# ============================
# Query Vectors
# ============================

def query_vectors(
    vector: list[float],
    top_k: int = 3
) -> list[dict]:
    """
    Searches Pinecone for similar vectors.
    """

    response = index.query(
        vector=vector,
        top_k=top_k,
        include_metadata=True
    )

    return response.matches
