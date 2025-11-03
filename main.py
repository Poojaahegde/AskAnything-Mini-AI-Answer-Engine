import streamlit as st
import wikipedia
from transformers import pipeline

st.set_page_config(page_title="AskAnything", page_icon="🤖")

st.title("AskAnything 🤖")
st.write("A mini AI-powered Q&A engine built using Wikipedia search and transformers summarization.")

query = st.text_input("Ask a question:")
if query:
    try:
        summary = ""
        results = wikipedia.search(query, results=3)
        st.write("### Sources:")
        for r in results:
            st.write(f"- {r}")
            page = wikipedia.page(r)
            summary += page.content[:1000]
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        answer = summarizer(summary, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        st.subheader("Answer:")
        st.write(answer)
    except Exception as e:
        st.error(f"Error: {e}")
