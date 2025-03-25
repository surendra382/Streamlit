import streamlit as st
import time

if 'messages' not in st.session_state:
    st.session_state.messages = []

def generate_response(user_input):
    response = """
        Jodhpur is the second-largest city of the north-western Indian state of Rajasthan after its capital Jaipur. As of 2023, the city has a population of 1.83 million.[11] It serves as the administrative headquarters of the Jodhpur district and Jodhpur division. It is historic capital of the Kingdom of Marwar, founded in 1459 by Rao Jodha, a Rajput chief of the Rathore clan.[12] On 11 August 1947, 4 days prior to the Indian independence, Maharaja Hanwant Singh the last ruler of Jodhpur state signed the Instrument of Accession and merged his state in Union of India.[13] On 30 March 1949, it became part of the newly formed state of Rajasthan, which was created after merging the states of the erstwhile Rajputana Agency    """
    for token in response.split(" "):
        time.sleep(0.01)
        yield token + " "

for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").markdown(message["content"])
    else:
        st.chat_message("ai").markdown(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input and user_input != "":
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("ai"):
        response_generator = generate_response(user_input)
        response = st.write_stream(response_generator)

    st.session_state.messages.append({"role": "bot", "content": response})