import json
import networkx as nx

def normalize(text):
    return text.lower().strip()

def build_graph(triples_path):
    G = nx.DiGraph()

    with open(triples_path, "r", encoding="utf-8") as f:
        triples = json.load(f)

    for t in triples:
        subject = t.get("subject")
        relation = t.get("relation") or t.get("predicate")  # ✅ KEY FIX
        obj = t.get("object")

        if not subject or not relation or not obj:
            continue

        subject = normalize(subject)
        obj = normalize(obj)

        G.add_edge(subject, obj, relation=relation)

    print(f"✅ Graph built with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")

    return G