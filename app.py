import streamlit as st

from graph.build_graph import build_graph
from retrieval.entity_extractor import extract_entities
from retrieval.query_graph import query_graph
from retrieval.context_builder import build_context
from llm.generate import generate_answer

DATA_PATH = "data/triples.json"

st.set_page_config(page_title="KG-RAG", page_icon="🧠")

st.title("🧠 Knowledge Graph RAG")
st.write("Ask questions based on the knowledge graph")

# load graph once
@st.cache_resource
def load_graph():
    return build_graph(DATA_PATH)

G = load_graph()

query = st.text_input("Ask a question:")

if query:
    # 1. entities
    entities = extract_entities(query)

    # 2. retrieve
    results = []
    for ent in entities:
        results.extend(query_graph(G, ent, query))

    # 3. context
    context = build_context(results)

    # 4. answer
    with st.spinner("Thinking..."):
        answer = generate_answer(context, query)

    # display
    st.subheader("🤖 Answer")
    st.write(answer)

    with st.expander("🔎 Context"):
        st.write(context)

    with st.expander("🧩 Entities"):
        st.write(entities)