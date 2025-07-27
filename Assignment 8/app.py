import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

# Debug
st.write("KEY from ENV:", os.getenv("OPENAI_API_KEY"))

import streamlit as st
from rag_pipeline import load_rag_pipeline

st.set_page_config(page_title="Loan RAG Chatbot", layout="wide")
st.title("Loan Approval Q&A Chatbot")
st.markdown("Ask any question based on the loan data:")

qa_chain = load_rag_pipeline()

query = st.text_input("Your question:", "")

if query:
    with st.spinner("Fetching answer..."):
        response = qa_chain.invoke({"query": query})
        st.write("Answer:")
        st.success(response['result'])

