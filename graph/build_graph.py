import json
import networkx as nx

def build_graph(triples_path):
    G = nx.DiGraph()

    with open(triples_path, "r") as f:
        triples = json.load(f)

    for t in triples:
        subject = t["subject"]
        relation = t["relation"]
        obj = t["object"]

        G.add_edge(subject, obj, relation=relation)

    print(f"✅ Graph built with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")

    return G


if __name__ == "__main__":
    G = build_graph("data/triples.json")