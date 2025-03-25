import streamlit as st

st.title('My first app')

st.write('Here\'s our first attempt at using data to create a table:')

# Display Text (and magic)
# Add Interactive Widgets
# Button
# Slider
# Text Input
# Data Visualizations
# Model Integration (AI/ML)
# Layouts and Columns

st.header('Display Text')
st.subheader('Display Markdown')


#Interactive widgets
#buttons
st.button('Simple Button')
if st.button('Button with Magic'):
    st.write('Magic')

#slider
import streamlit as st
import numpy as np
import pandas as pd

st.title('Plot Function')
power = st.slider('Select the power of x', 1, 10, 2)

# fix axis range
x = np.linspace(-10, 10, 100)
y = x**power

st.line_chart(pd.DataFrame(y, x), use_container_width=True)

#text input
name = st.text_input('Enter your name:')
st.write('Hello,', name)

#Data visualizations
import streamlit as st
import numpy as np
import pandas as pd
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

import pandas as pd
import numpy as np
data = pd.DataFrame({
    'X': np.random.randn(100),
    'Y': np.random.randn(100)
})
st.line_chart(data)

# #Model Integration
# import streamlit as st
# from transformers import pipeline
# # Load the T5 model for summarization
# @st.cache_resource(show_spinner="Loading model...")
# def load_model():
#     summarizer = pipeline("summarization", model="t5-base")
#     return summarizer
# summarizer = load_model()
# # Streamlit app title
# st.title("Text Summarization App")
# # User input text area
# user_input = st.text_area("Enter text to summarize:")
# # Perform summarization when the user clicks the button
# if st.button("Summarize"):
#     if user_input:
#         # Perform summarization
#         summary = summarizer(user_input, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
# # Display the result
#         st.write("***Summary:***")
#         st.write(summary)
#     else:
#         st.write("Please enter some text to summarize.")

#layouts
col1, col2 = st.columns((1,2))

with col1:
  st.write("Column 1 content 111111111111111111111111111111111111")

with col2:
  st.write("Column 2 content2222222222222222222222222222222222222")

#Sidebar:
# st.sidebar.title("Sidebar Title")
# st.sidebar.button("Click Here")
st.sidebar.expander("Click Here to expand", expanded=True)








