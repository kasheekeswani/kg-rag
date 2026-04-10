def extract_entities(text):
    words = text.replace("?", "").split()

    stopwords = {
        "what", "is", "the", "did", "who", "in", "for",
        "of", "on", "at", "a", "an", "work"
    }

    # keep only meaningful words
    entities = [w for w in words if w.lower() not in stopwords and len(w) > 2]

    return entities