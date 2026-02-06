from api.confidence import evaluate_confidence
from api.wikipedia import wikipedia_fallback
from ai.llm import generate_answer
from vectorstore.pinecone_client import vectorstore

def answer_query(query: str) -> str:
    docs = vectorstore.similarity_search(query, k=3)
    context = "\n\n".join(d.page_content for d in docs)

    confidence = evaluate_confidence(query, context)

    if confidence.score < 0.6:
        wiki_text = wikipedia_fallback(query)
        if wiki_text:
            return generate_answer(
                context=wiki_text,
                source="wikipedia"
            )

    return generate_answer(
        context=context,
        source="government_pdf"
    )
