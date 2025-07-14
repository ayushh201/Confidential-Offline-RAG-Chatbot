# Streamlit UI entry point
import streamlit as st
from rag_pipeline import query_rag

st.set_page_config(page_title="Offline RAG Chatbot", layout="wide")
st.title("🔒 Confidential RAG Chatbot")

question = st.text_input("Enter your question:")

if question:
    with st.spinner("Thinking..."):
        answer, context = query_rag(question)
        st.markdown("### 💬 Answer:")
        st.success(answer)
        with st.expander("🔍 Show context chunks"):
            st.write(context)