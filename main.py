from graph.build_graph import build_graph
from retrieval.entity_extractor import extract_entities
from retrieval.query_graph import query_graph
from retrieval.context_builder import build_context

DATA_PATH = "data/triples.json"


def main():
    print("🧠 KG-RAG System (type 'exit' to quit)\n")

    # build graph once
    G = build_graph(DATA_PATH)

    while True:
        query = input("\nAsk: ")

        if query.lower() == "exit":
            break

        # 1. extract entities
        entities = extract_entities(query)
        print("Entities:", entities)

        # 2. retrieve from graph
        results = []
        for ent in entities:
            results.extend(query_graph(G, ent))

        # limit results (important)
        results = results[:10]

        # 3. build context
        context = build_context(results)

        print("\nContext:")
        print(context)


if __name__ == "__main__":
    main()