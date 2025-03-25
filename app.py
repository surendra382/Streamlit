# Introduction to Streamlit Chat Widgets
# Streamlit’s chat widgets allow developers to create 
# real-time, interactive chat interfaces within Streamlit
# apps. With these widgets, you can simulate a 
# conversation flow between the user and an AI-powered 
# backend, such as OpenAI’s GPT models.

# Streamlit provides two main functions for chat-based 
# interfaces:

# st.chat_message(): Displays a message in the chat 
# interface.

# st.chat_input(): Takes user input in a chat-like format

# # In this lesson, we’ll build a conversational 
# assistant using these widgets and the OpenAI API to 
# generate responses.

#requirement:
#we need something to take user input (chat_input)
#we need send that input to llm
# we need store that in memory (session state)
# we need to show response from llm to user on screen/app (chat_message
# we also need to store that response in memory

import streamlit as st
import time

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").markdown(message["content"])
    else:
        st.chat_message("ai").markdown(message["content"])

def generate_response(user_input):
    response = """
    Saran AI Labs is an innovative initiative by Surendra Saran Choudhary, focused on advancing knowledge in the field of AI and Generative AI.
	It aims to bridge the gap between academic learning and real-world applications of AI technologies.
	The lab offers hands-on training programs, workshops, and courses tailored for students, professionals, and AI enthusiasts.
	Its flagship 12-week Generative AI course empowers participants to build LLM-based applications and explore industry-relevant use cases.
	The lab provides access to session recordings, source code, and interactive doubt-solving sessions.
	Saran AI Labs emphasizes practical learning with end-to-end project life cycle implementation and exposure to real-life projects.
	The initiative organizes free workshops and affordable events to inspire and educate college students about AI advancements.
	It fosters a collaborative community through its WhatsApp group, "GenAI Gems," connecting AI enthusiasts across industries.
	The lab also offers a referral program, encouraging community growth and rewarding advocates of the initiative.
	Saran AI Labs aspires to be a leading platform for cultivating AI talent and driving innovation in generative AI solutions.
    """

    for token in response.split(" "):
        time.sleep(0.01)
        yield token + " "

user_input = st.chat_input("Type your message here...")

if user_input and user_input != "":

    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("ai"):
      response_generator = generate_response(user_input)
      response = st.write_stream(response_generator)


    
    st.session_state.messages.append({"role": "bot", "content": response})





















































