import streamlit as st

# Initialize session state for chat history and input
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to handle new chat input
def handle_user_input():
    user_input = st.session_state.user_input
    if user_input:
        # Append user message to session state
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Simple bot response logic
        response = user_input[::-1] # Reverse the user input for fun
        st.session_state.messages.append({"role": "bot", "content": response})

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message("bot"):
            st.write(message["content"])

# Input widget for user to send messages
#st.chat_input("Your message", key="user_input", on_submit=handle_user_input)
st.chat_input("Your message", key="user_input", on_submit=handle_user_input)