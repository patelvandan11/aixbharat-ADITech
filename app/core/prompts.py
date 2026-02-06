CONFIDENCE_PROMPT = """
You are an evaluator.

Question:
{question}

Retrieved Information:
{context}

Evaluate how well the retrieved information answers the question.

Return:
- score: float between 0 and 1
- reason: short explanation
"""
