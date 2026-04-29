def extract_entities(text):
    text = text.replace("?", "")

    stopwords = {
        "what", "is", "the", "did", "who", "in", "for",
        "of", "on", "at", "a", "an", "work", "known"
    }

    words = text.split()

    entities = []
    current = []

    for w in words:
        if w.lower() not in stopwords:
            current.append(w)
        else:
            if current:
                entities.append(" ".join(current))
                current = []

    if current:
        entities.append(" ".join(current))

    return entities