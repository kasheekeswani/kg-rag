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

    # -------------------------
    # 1. Strong entity match
    # -------------------------
    if entity == u_norm:
        score += 6
    elif entity in u_norm:
        score += 4

    # -------------------------
    # 2. Question relevance
    # -------------------------
    score += similarity(u_norm, q_norm) * 2
    score += similarity(v_norm, q_norm)

    # -------------------------
    # 3. Relation importance (FIXED)
    # -------------------------
    if relation == "is_a":
        score += 4
    elif relation == "has_iupac_name":
        score += 2
    elif relation == "has_synonym":
        score += 2
    elif relation == "has_molecular_weight":
        score += 1

    return score


def query_graph(G, entity, question):
    scored_results = []

    for u, v, data in G.edges(data=True):
        relation = data.get("relation")  # ✅ FIXED

        if not relation:
            continue

        score = score_edge(u, relation, v, entity, question)

        if score > 0:  # ✅ less strict
            scored_results.append((score, u, relation, v))

    # Sort by score
    scored_results.sort(reverse=True, key=lambda x: x[0])

    # Return top results (without score)
    top_results = [(u, r, v) for score, u, r, v in scored_results[:10]]

    return top_results