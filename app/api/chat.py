from ai.rag import answer_query

def chat_handler(message: str) -> str:
    """
    Handles a user query and returns a final response.
    """

    response = answer_query(message)
    return response
