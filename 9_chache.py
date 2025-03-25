import streamlit as st
import requests
import time

@st.cache_data (max_entries=10,max_entries=10)
def fetch_data(api_url):
    response = requests.get(api_url)
    time.sleep(5)
    return response.json()
data = fetch_data("https://dog.ceo/api/breeds/image/random")
st.write(data)
st.image(data["message"], caption="Random dog image")
st.button("Reload page")

import streamlit as st
import time
class AiModel:
    def __init__(self):
        # Load model
        time.sleep(5)
        self.model = "model"
def predict(self, input_data):
        return "prediction"
@st.cache_resource(show_spinner="Loading Model...")
def load_model():
    model = AiModel()
    return model
model = load_model()
if model:
    st.write("Model Loaded")
st.button("reload page")