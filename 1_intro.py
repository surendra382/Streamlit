
import streamlit as st

prompt = st.chat_input("What's your name?")
if prompt:
    st.write(f"Hello, {prompt}! How can I help you today?")