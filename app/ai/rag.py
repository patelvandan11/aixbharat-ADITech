from app.ai.confidence import evaluate_confidence
from app.ai.wikipedia import search_wikipedia

docs = vectorstore.similarity_search(query, k=3)
context = "\n\n".join([d.page_content for d in docs])

confidence = evaluate_confidence(query, context)

if confidence.score < 0.6:
    wiki_text = search_wikipedia(query)
    answer = llm_answer(wiki_text, source="wikipedia")
else:
    answer = llm_answer(context, source="government_pdf")
