def query_graph(G, entity):
    results = []

    entity = entity.lower()

    for u, v, data in G.edges(data=True):
        if entity == u.lower() or entity == v.lower():
            results.append((u, data["relation"], v))

        # allow partial match only for longer words
        elif len(entity) > 4 and entity in u.lower():
            results.append((u, data["relation"], v))

    return results