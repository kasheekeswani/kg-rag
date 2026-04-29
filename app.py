import streamlit as st

from graph.build_graph import build_graph
from retrieval.entity_extractor import extract_entities
from retrieval.query_graph import query_graph
from retrieval.context_builder import build_context
from llm.generate import generate_answer

DATA_PATH = "data/triples1.json"  # ✅ make sure this matches your latest file

st.set_page_config(page_title="KG-RAG", page_icon="🧠")

st.title("🧠 Knowledge Graph RAG")
st.write("Ask questions based ONLY on the knowledge graph")

# -------------------------
# Load graph once
# -------------------------
@st.cache_resource
def load_graph():
    return build_graph(DATA_PATH)

G = load_graph()

# -------------------------
# User input
# -------------------------
query = st.text_input("Ask a question:")

if query:
    # -------------------------
    # 1. Extract entities
    # -------------------------
    entities = extract_entities(query)

    st.expander("🧩 Entities").write(entities)

    if not entities:
        st.warning("⚠️ Could not extract entities from question")
        st.stop()

    # -------------------------
    # 2. Retrieve from graph
    # -------------------------
    results = []
    for ent in entities:
        results.extend(query_graph(G, ent, query))

    # remove duplicates
    results = list(set(results))

    if not results:
        st.warning("⚠️ No relevant data found in knowledge graph")
        st.stop()

    # -------------------------
    # 3. Build context
    # -------------------------
    context = build_context(results)

    if not context or context.strip() == "":
        st.warning("⚠️ Context is empty")
        st.stop()

    # -------------------------
    # 4. Generate answer
    # -------------------------
    with st.spinner("Thinking..."):
        answer = generate_answer(context, query)

    # -------------------------
    # Display
    # -------------------------
    st.subheader("🤖 Answer")
    st.write(answer)

    with st.expander("🔎 Context"):
        st.write(context)