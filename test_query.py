from app.ai.embeddings import generate_embedding
from app.vectorstore.pinecone_client import query_vectors

query = "How to apply for Aadhaar?"
vec = generate_embedding(query)

results = query_vectors(vec)

print(results[0]["metadata"]["source"])
print(results[0]["metadata"]["text"][:300])
