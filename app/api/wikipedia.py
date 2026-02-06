import wikipedia

def wikipedia_fallback(query: str) -> str | None:
    """
    Fetches a short Wikipedia summary for general information.
    Used only as a fallback.
    """

    try:
        wikipedia.set_lang("en")
        return wikipedia.summary(query, sentences=5)

    except wikipedia.exceptions.DisambiguationError as e:
        return wikipedia.summary(e.options[0], sentences=5)

    except Exception:
        return None
