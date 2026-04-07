def query_graph(G, entity):
    results = []

    for u, v, data in G.edges(data=True):
        if entity.lower() in u.lower() or entity.lower() in v.lower():
            results.append((u, data["relation"], v))

    return results