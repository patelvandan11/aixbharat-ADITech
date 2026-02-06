from app.ai.llm import generate_answer
from app.ai.embeddings import generate_embedding

vec = generate_embedding("Ayushman Bharat is a health insurance scheme.")
print(len(vec))

print(
    generate_answer(
        question="What is Ayushman Bharat?",
        context="Ayushman Bharat is a health insurance scheme launched by the Government of India.",
        source="wikipedia"
    )
)
