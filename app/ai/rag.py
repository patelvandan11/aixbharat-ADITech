from typing import List

from app.ai.embeddings import generate_embedding
from app.vectorstore.pinecone_client import query_vectors
from app.api.confidence import evaluate_confidence
from app.api.wikipedia import wikipedia_fallback
from app.ai.llm import generate_answer
from app.core.config import CONFIDENCE_THRESHOLD


def _build_context_from_matches(matches: List[dict]) -> str:
    """
    Builds a text context from Pinecone search results.
    """

    contexts = []

    for match in matches:
        metadata = match.get("metadata", {})
        text = metadata.get("text")
        if text:
            contexts.append(text)

    return "\n\n".join(contexts)


# def answer_query(question: str) -> str:
#     """
#     Main RAG entry point.
#     """

#     # 1️⃣ Generate embedding for the query
#     query_embedding = generate_embedding(question)

#     # 2️⃣ Search Pinecone
#     matches = query_vectors(query_embedding, top_k=3)

#     # 3️⃣ If nothing found → Wikipedia fallback
#     if not matches:
#         wiki_text = wikipedia_fallback(question)
#         if wiki_text:
#             return generate_answer(
#                 question=question,
#                 context=wiki_text,
#                 source="wikipedia"
#             )
#         return "Sorry, I could not find relevant information."

#     # 4️⃣ Build context from PDF matches
#     context = _build_context_from_matches(matches)

#     # 5️⃣ Evaluate confidence
#     confidence = evaluate_confidence(
#         question=question,
#         retrieved_context=context
#     )

#     # 6️⃣ Decide source
#     if confidence.score < CONFIDENCE_THRESHOLD:
#         wiki_text = wikipedia_fallback(question)
#         if wiki_text:
#             return generate_answer(
#                 question=question,
#                 context=wiki_text,
#                 source="wikipedia"
#             )

#     # 7️⃣ Generate final answer using PDFs
#     return generate_answer(
#         question=question,
#         context=context,
#         source="government_pdf"
#     )

def answer_query(question: str) -> str:
    print("🔹 Question:", question)

    query_embedding = generate_embedding(question)
    print("🔹 Embedding length:", len(query_embedding))

    matches = query_vectors(query_embedding, top_k=3)
    print("🔹 Pinecone matches:", len(matches))

    if not matches:
        print("⚠️ No Pinecone matches → Wikipedia fallback")
        wiki_text = wikipedia_fallback(question)
        print("🔹 Wikipedia text:", wiki_text[:200] if wiki_text else None)

        if wiki_text:
            return generate_answer(
                question=question,
                context=wiki_text,
                source="wikipedia"
            )

        return "❌ No information found."

    context = _build_context_from_matches(matches)
    print("🔹 Context length:", len(context))

    confidence = evaluate_confidence(
        question=question,
        retrieved_context=context
    )

    print("🔹 Confidence score:", confidence.score)
    print("🔹 Confidence reason:", confidence.reason)

    if confidence.score < CONFIDENCE_THRESHOLD:
        print("⚠️ Low confidence → Wikipedia fallback")
        wiki_text = wikipedia_fallback(question)

        if wiki_text:
            return generate_answer(
                question=question,
                context=wiki_text,
                source="wikipedia"
            )

    print("✅ Using PDF context")
    return generate_answer(
        question=question,
        context=context,
        source="government_pdf"
    )
