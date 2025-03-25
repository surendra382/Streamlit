import streamlit as st
from transformers import pipeline

# Load the T5 model for summarization
@st.cache_resource(show_spinner="Loading model...")
def load_model():
    summarizer = pipeline("summarization", model="t5-base")
    return summarizer
summarizer = load_model()

# Streamlit app title
st.title("Text Summarization App")

# User input text area
user_input = st.text_area("Enter text to summarize:")

# Perform summarization when the user clicks the button
if st.button("Summarize"):
    if user_input:
        # Perform summarization
        summary = summarizer(user_input, max_length=150, min_length=30, do_sample=False)[0]['summary_text']

        # Display the result
        st.write("**Summary:**")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")