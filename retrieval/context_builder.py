def build_context(results):
    if not results:
        return "No relevant information found."

    known_for = []
    works_in = []

    for u, r, v in results:
        if r == "known_for":
            known_for.append(v)
        elif r == "works_in":
            works_in.append(v)

    context = ""

    if known_for:
        context += f"{u} is known for: {', '.join(known_for)}. "

    if works_in:
        context += f"{u} worked in: {', '.join(works_in)}."

    return context