from graph.build_graph import build_graph
from retrieval.entity_extractor import extract_entities
from retrieval.query_graph import query_graph
from retrieval.context_builder import build_context
from llm.generate import generate_answer

DATA_PATH = "data/triples.json"


def main():
    print("🧠 KG-RAG System (type 'exit' to quit)\n")

    G = build_graph(DATA_PATH)

    while True:
        query = input("\nAsk: ")

        if query.lower() == "exit":
            break

        # 1. extract entities
        entities = extract_entities(query)

        # 2. retrieve
        results = []
        for ent in entities:
            results.extend(query_graph(G, ent))

        results = results[:10]

        # 3. build context
        context = build_context(results)

        print("\n🔎 Context:")
        print(context)

        # 4. generate answer
        answer = generate_answer(context, query)

        print("\n🤖 Answer:")
        print(answer)


if __name__ == "__main__":
    main()