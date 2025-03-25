import streamlit as st

messages = []

for message in messages:
    if message["role"] == "user":
        st.chat_message("user").markdown(message["content"])
    else:
        st.chat_message("ai").markdown(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input and user_input != "":
    st.chat_message("user").markdown(user_input)
    messages.append({"role": "user", "content": user_input})
    bot_response = f"Echo: {user_input}"
    st.chat_message("ai").markdown(bot_response)
    messages.append({"role": "bot", "content": bot_response})