import wikipedia

def search_wikipedia(query: str, sentences: int = 5):
    try:
        wikipedia.set_lang("en")
        summary = wikipedia.summary(query, sentences=sentences)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return wikipedia.summary(e.options[0], sentences=sentences)
    except Exception:
        return None
