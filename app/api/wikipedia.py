from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper


# Configure Wikipedia API
wiki_api = WikipediaAPIWrapper(
    top_k_results=3,
    doc_content_chars_max=1500
)

wiki_tool = WikipediaQueryRun(api_wrapper=wiki_api)


def wikipedia_fallback(query: str) -> str:
    """
    Uses LangChain Wikipedia retriever to get reliable context.
    Always returns text.
    """

    try:
        result = wiki_tool.run(query)

        if result and result.strip():
            return result

    except Exception:
        pass

    # Absolute safety fallback
    return f"General public information about {query}."
