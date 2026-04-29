def normalize(text):
    return text.lower().replace("-", " ").strip()


def similarity(a, b):
    a_words = set(normalize(a).split())
    b_words = set(normalize(b).split())

    if not a_words or not b_words:
        return 0

    return len(a_words & b_words) / len(a_words | b_words)


def score_edge(u, relation, v, entity, question):
    score = 0

    entity = normalize(entity)
    u_norm = normalize(u)
    v_norm = normalize(v)
    q_norm = normalize(question)

    # exact match boost
    if entity == u_norm:
        score += 5

    # partial match
    if entity in u_norm:
        score += 3

    # semantic similarity with question
    score += similarity(u_norm, q_norm) * 2
    score += similarity(v_norm, q_norm)

    # relation priority
    if relation == "known_for":
        score += 3
    elif relation == "works_in":
        score += 1

    return score


def query_graph(G, entity, question):
    scored_results = []

    for u, v, data in G.edges(data=True):
        relation = data["relation"]

        score = score_edge(u, relation, v, entity, question)

        if score > 1:  # filter weak matches
            scored_results.append((score, u, relation, v))

    # sort by score (highest first)
    scored_results.sort(reverse=True, key=lambda x: x[0])

    # ✅ FIX: remove score before returning
    top_results = [(u, r, v) for score, u, r, v in scored_results[:8]]

    return top_results