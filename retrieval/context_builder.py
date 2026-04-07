def build_context(results):
    if not results:
        return "No relevant information found."

    sentences = []
    for u, r, v in results:
        sentences.append(f"{u} {r} {v}")

    return ". ".join(sentences)