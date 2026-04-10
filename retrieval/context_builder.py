def build_context(results):
    if not results:
        return "No relevant information found."

    sentences = []
    seen = set()

    for u, r, v in results:
        sentence = f"{u} {r} {v}"
        if sentence not in seen:
            seen.add(sentence)
            sentences.append(sentence)

    return ". ".join(sentences[:8])  # limit size