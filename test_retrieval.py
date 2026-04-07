from graph.build_graph import build_graph
from retrieval.query_graph import query_graph
from retrieval.entity_extractor import extract_entities
from retrieval.context_builder import build_context

# build graph
G = build_graph("data/triples.json")

# test query
query = "What is Galileo known for?"

# extract entities
entities = extract_entities(query)
print("Entities:", entities)

# query graph
results = []
for ent in entities:
    results.extend(query_graph(G, ent))

print("Results:", results[:5])

# build context
context = build_context(results)
print("\nContext:\n", context)