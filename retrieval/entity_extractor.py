def extract_entities(text):
    # simple keyword-based extraction
    words = text.replace("?", "").split()

    # remove common words
    stopwords = {"what", "is", "the", "did", "who", "in", "for", "of"}

    entities = [w for w in words if w.lower() not in stopwords]

    return entities