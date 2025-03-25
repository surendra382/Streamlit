import streamlit as st

if 'messages' not in st.session_state:
    st.session_state.messages = []

def handle_userinput():
    user_input = st.session_state.user_input
    if user_input and user_input != "":
        #st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        bot_response = f"Echo: {user_input}"
        #st.chat_message("ai").markdown(bot_response)
        st.session_state.messages.append({"role": "bot", "content": bot_response})

for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").markdown(message["content"])
    else:
        st.chat_message("ai").markdown(message["content"])

st.chat_input("Type your message here...", key="user_input", on_submit=handle_userinput)




#Callback functions
#widgets, events, function

