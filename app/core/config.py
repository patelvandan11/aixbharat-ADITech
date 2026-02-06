import os
from dotenv import load_dotenv
# Load .env file
load_dotenv()
# =========================
# OpenAI Configuration
# =========================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_CHAT_MODEL = os.getenv(
    "OPENAI_CHAT_MODEL",
    "gpt-4.1-mini"
)

OPENAI_EMBEDDING_MODEL = os.getenv(
    "OPENAI_EMBEDDING_MODEL",
    "text-embedding-3-small"
)
# =========================
# Pinecone Configuration
# =========================
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
PINECONE_INDEX_NAME = os.getenv(
    "PINECONE_INDEX_NAME",
    "aixbharat"
)
# =========================
# Confidence Threshold
# =========================
CONFIDENCE_THRESHOLD = float(
    os.getenv("CONFIDENCE_THRESHOLD", "0.6")
)
# =========================
# Validation (Fail Fast)
# =========================
missing_vars = []

if not OPENAI_API_KEY:
    missing_vars.append("OPENAI_API_KEY")

if not PINECONE_API_KEY:
    missing_vars.append("PINECONE_API_KEY")

if not PINECONE_ENV:
    missing_vars.append("PINECONE_ENV")

if missing_vars:
    raise RuntimeError(
        f"Missing required environment variables: {', '.join(missing_vars)}"
    )
