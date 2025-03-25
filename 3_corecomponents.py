
import streamlit as st

#1_Display text
st.title("hello streamlit")
st.header("This is a header")
st.subheader("This is a subheader")
st.write("This is your first streamlit app")#for writing output


import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [40, 50, 60]})
df
st.table(df)
st.write(df)
st.dataframe(df)

#2. Add Interactive Widgets
#2.1 Button
if st.button("Say hello"):
    st.write("Why hello there")

#2.2 Slider
import streamlit as st
import numpy as np
import pandas as pd

st.title('Plot Function')
power = st.slider('Select the power of x', 1, 10, 2)

# fix axis range
x = np.linspace(-10, 10, 100)
y = x**power

st.line_chart(pd.DataFrame(y, x), use_container_width=True)

#2.3 Text Input:
name = st.text_input('Enter your name:')
st.write('Hello,', name)

##3. Data Visualizations
#3.1 map
import streamlit as st
import numpy as np
import pandas as pd
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)

#3.2 Line chart, bar chart
import pandas as pd
import numpy as np
data = pd.DataFrame({
    'X': np.random.randn(100),
    'Y': np.random.randn(100)
})
st.line_chart(data)

##4 Model Interactions
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


##5 Layout, creating columns with first column width as 1 and second column width as 2    
#5.1 Columns
col1, col2 = st.columns((1, 4))
#col1, col2 = st.columns(1,2)
col1.write("This is column 111111111111111111111111111111111111111111111111111111")
col2.write("This is column 222222222222222222222222222222222222222222222222222222")

#5.3 Sidebar
st.sidebar.title("Configuration")

#5.2 Expander
with st.sidebar.expander("Choose color"):
    value = st.radio("What is your favorite color?", ("Red", "Green", "Blue"))
    st.write(value)

