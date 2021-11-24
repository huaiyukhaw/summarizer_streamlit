import streamlit as st
from transformers import pipeline
import webbrowser

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
st.title("Summarizer")

col1, col2 = st.columns(2)
article = col1.text_area("Write something", height=450)
submitted = col1.button("Submit")

if submitted:
    col2.write("Output")
    prediction = summarizer(article, max_length=250,
                            min_length=30, do_sample=False)[0]["summary_text"]
    col2.write(prediction)
    col2.markdown(f"[Tweet this](https://twitter.com/intent/tweet?text={prediction.replace(' ', '%20')})", unsafe_allow_html=True)
