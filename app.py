import streamlit as st
from rag_pipeline import get_answer

st.title("📦 Gen AI product Search Bot")

query = st.text_input("Ask a product-related question:")

if st.button("Get Answer") and query:
    answer, sources = get_answer(query)
    st.subheader("Answer:")
    st.write(answer)
    st.subheader("Sources:")
    for s in sources:
        st.code(s)
