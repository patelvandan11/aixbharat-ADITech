from pinecone import Pinecone
from app.core.config import PINECONE_API_KEY, PINECONE_INDEX_NAME

pc = Pinecone(api_key=PINECONE_API_KEY)

pc.delete_index(PINECONE_INDEX_NAME)
print("✅ Index deleted")
