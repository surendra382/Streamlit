# Streamlit Fundamentals

## 📌 Introduction

**Streamlit** is a powerful Python library used to build web apps easily and efficiently—especially useful for data scientists, AI/ML practitioners, and researchers.

It helps in:
- Creating intuitive GUIs for AI/ML applications.
- Documenting and demoing models via websites or APIs.
- Prototyping interactive apps rapidly.
- Integrating with AI/ML pipelines.
- Creating chat apps using chat widgets.

### ⚡ Why Use Streamlit?
- **Ease of Use**: Python-first and beginner-friendly.
- **Real-time Interactivity**: Automatically reruns script on user input.
- **Fast Prototyping**: Ideal for dashboards and model demos.
- **ML/AI Friendly**: Built for rapid model integration.

---

## 🚀 Getting Started with Streamlit

### 🔧 Installation
```bash
pip install streamlit
```

### 📝 Create a Basic App
```python
# app.py
import streamlit as st

st.title('Hello, Streamlit!')
st.write('This is your first Streamlit app.')
```

### ▶️ Run Your App
```bash
streamlit run app.py
```
Visit [http://localhost:8501](http://localhost:8501) to see your app.

---

## 🧱 Core Components

### 📄 Displaying Text
```python
st.title('App Title')
st.header('Subsection')
st.text('Simple text')
st.write('Flexible writer')
```

```python
# Automatically renders a DataFrame
import pandas as pd
st.write(pd.DataFrame({"A": [1,2], "B": [3,4]}))
```

### 🎛️ Interactive Widgets
```python
# Button
if st.button('Click Me'):
    st.write('Button clicked!')

# Slider
power = st.slider('Power of x', 1, 10, 2)

# Text input
name = st.text_input('Enter your name:')
st.write(f'Hello, {name}!')
```

### 📊 Visualizations
```python
import pandas as pd
import numpy as np

# Built-in charts
data = pd.DataFrame({'x': range(100), 'y': np.random.randn(100)})
st.line_chart(data)

# Map chart
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)
```

### 🤖 Model Integration (AI/ML)
```python
# Sentiment summarization example
from transformers import pipeline
@st.cache_resource(show_spinner="Loading model...")
def load_model():
    return pipeline("summarization", model="t5-base")

summarizer = load_model()
user_input = st.text_area("Enter text to summarize:")
if st.button("Summarize") and user_input:
    summary = summarizer(user_input, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    st.write("**Summary:**")
    st.write(summary)
```

---

## 📐 Layouts and UI Structure

### Columns
```python
col1, col2 = st.columns(2)
with col1:
    st.write("Left")
with col2:
    st.write("Right")
```

### Sidebar
```python
st.sidebar.title("Controls")
st.sidebar.button("Reset")
```

---

## 💬 Streamlit Chat Components

### Chat Interface
```python
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Chat input
user_input = st.chat_input("Say something...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    bot_response = f"Echo: {user_input}"
    st.chat_message("ai").markdown(bot_response)
    st.session_state.messages.append({"role": "ai", "content": bot_response})
```

Run using:
```bash
streamlit run chat_app.py
```

---

## 🔁 Streaming Chat in Streamlit
```python
import time

def generate_response(text):
    for word in text.split():
        time.sleep(0.01)
        yield word + " "

with st.chat_message("ai"):
    st.write_stream(generate_response("This is a streaming response."))
```

---

## 🔄 Streamlit Data Flow

Streamlit reruns the full script on any interaction. This can cause:
- Redundant API calls
- Recomputed heavy models

Use **Session State** and **Caching** to optimize.

---

## 📌 Session State & Callback Functions

### Session State Example
```python
if "messages" not in st.session_state:
    st.session_state.messages = []

def handle_user_input():
    user_input = st.session_state.user_input
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "bot", "content": user_input[::-1]})

for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

st.chat_input("Your message", key="user_input", on_submit=handle_user_input)
```

### Callbacks with Args
```python
def handle_input(msg, bot_name="Bot", mood="neutral"):
    st.write(f"{bot_name} ({mood}): You said '{msg}'")

st.button("Send", on_click=handle_input, args=("Hello",), kwargs={"bot_name": "AI", "mood": "happy"})
```

---

## 🧠 Caching in Streamlit

Caching helps avoid redundant computations and API calls.

### Types:
- `@st.cache_data`: For serializable outputs like JSON or DataFrames.
- `@st.cache_resource`: For objects like ML models.

### Example: Caching API Results
```python
import requests
@st.cache_data
def fetch_data():
    return requests.get("https://dog.ceo/api/breeds/image/random").json()

data = fetch_data()
st.image(data["message"])
```

### Example: Caching a Model
```python
import time
class AiModel:
    def __init__(self):
        time.sleep(5)  # simulate delay
        self.name = "MyModel"

@st.cache_resource(show_spinner="Loading model...")
def load_model():
    return AiModel()

model = load_model()
st.write(model.name)
```

### Custom Cache Options
```python
@st.cache_data(ttl=3600, max_entries=10)
def fetch_stock_data():
    pass
```

---

## ✅ Conclusion

Streamlit empowers Python developers to build **rich, interactive web applications** easily. By mastering widgets, chat interfaces, session management, and caching, you can build powerful, real-time ML or AI apps in minutes.

Happy coding! 🚀

