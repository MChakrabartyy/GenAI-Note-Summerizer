import streamlit as st
from app.summarizer import summarize_pdf

st.set_page_config(page_title="GenAI Note Summarizer", layout="wide")
st.title("📚 GenAI Note Summarizer")

uploaded_file = st.file_uploader("Upload your PDF notes", type="pdf")

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Summarizing with GPT-4..."):
        summary = summarize_pdf("temp.pdf")

    st.subheader(" Summary:")
    st.write(summary)
