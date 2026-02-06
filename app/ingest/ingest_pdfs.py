import logging
import uuid
from typing import List

from tqdm import tqdm

from app.text_spliting.text_spliter import load_and_split_documents
from app.ai.embeddings import generate_embedding
from app.vectorstore.pinecone_client import upsert_records

logger = logging.getLogger(__name__)


def ingest_pdfs_to_pinecone(
    data_folder: str = "app/data",
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
    batch_size: int = 100
) -> None:
    """
    Loads PDFs, splits them into chunks, generates embeddings,
    and stores them into Pinecone.
    """

    logger.info("🚀 Starting PDF ingestion process")

    documents = load_and_split_documents(
        data_folder=data_folder,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    if not documents:
        logger.warning("⚠️ No documents found to ingest")
        return

    vectors: List[dict] = []

    for doc in tqdm(documents, desc="Embedding & Uploading"):
        try:
            embedding = generate_embedding(doc.page_content)

            # Handle OpenAI-style response
            if isinstance(embedding, list) and isinstance(embedding[0], list):
                embedding = embedding[0]

            if len(embedding) != 1536:
                raise ValueError("Invalid embedding dimension")

        except Exception as e:
            logger.exception(f"❌ Embedding failed: {e}")
            continue

        vectors.append({
            "id": str(uuid.uuid4()),
            "values": embedding,
            "metadata": {
                "text": doc.page_content,
                "source": doc.metadata.get("source", "unknown")
            }
        })

        # Batch upload
        if len(vectors) >= batch_size:
            upsert_records(vectors)
            vectors.clear()

    # Upload remaining vectors
    if vectors:
        upsert_records(vectors)

    logger.info("✅ PDF ingestion completed successfully")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    ingest_pdfs_to_pinecone()
