"""
Community blogs API. Returns a list of blog entries for the frontend.
"""
from fastapi import APIRouter

router = APIRouter(tags=["blogs"])

# Seed data; can later be moved to PostgreSQL or a CMS
BLOGS = [
    {
        "id": 1,
        "title": "Using AI to make Aadhaar and government info easier to find",
        "summary": "How we're building a RAG-based assistant so people can ask questions in their language and get answers from official PDFs and notices.",
        "tags": ["aadhaar", "rag", "government", "multilingual"],
    },
    {
        "id": 2,
        "title": "Ayushman Bharat and health schemes in plain language",
        "summary": "Breaking down eligibility, documents, and application steps for health schemes so more families can access them.",
        "tags": ["health", "ayushman", "schemes", "access"],
    },
    {
        "id": 3,
        "title": "Local-language assistants for public impact",
        "summary": "Experiments with speech-to-text, translation, and local languages to bridge the gap between policy and communities.",
        "tags": ["speech", "translation", "local-language", "impact"],
    },
]


@router.get("/blogs")
def list_blogs():
    """Return all community blog entries."""
    return BLOGS
