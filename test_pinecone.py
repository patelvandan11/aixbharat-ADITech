from app.vectorstore.pinecone_client import upsert_vectors, query_vectors
from app.ai.embeddings import generate_embedding

vec = generate_embedding("Ayushman Bharat health insurance")

upsert_vectors([
    {
        "id": "test-1",
        "values": vec,
        "metadata": {"text": "Ayushman Bharat provides health insurance"}
    }
])

result = query_vectors(vec)
print(result)
print(f"Retrieved {len(result['matches'])} matches.")