from graph.build_graph import build_graph
from retrieval.entity_extractor import extract_entities
from retrieval.query_graph import query_graph
from retrieval.context_builder import build_context
from llm.generate import generate_answer

# 👉 SWITCH TO PUBCHEM GRAPH
DATA_PATH = "data/triples1.json"


def main():
    print("🧠 KG-RAG System (type 'exit' to quit)\n")

    G = build_graph(DATA_PATH)

    while True:
        query = input("\nAsk: ")

        if query.lower() == "exit":
            break

        # 1. Extract entities
        entities = extract_entities(query)
        print(f"\n🧩 Entities: {entities}")  # helpful debug

        # 2. Retrieve from graph
        results = []
        for ent in entities:
            results.extend(query_graph(G, ent, query))

        results = results[:10]

        if not results:
            print("\n⚠️ No results found in graph")
            continue

        # 3. Build context
        context = build_context(results)

        print("\n🔎 Context:")
        print(context)

        # 4. Generate answer
        answer = generate_answer(context, query)

        print("\n🤖 Answer:")
        print(answer)


if __name__ == "__main__":
    main()