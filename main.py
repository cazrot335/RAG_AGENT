import streamlit as st
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("HF_API_KEY")  # Store API key in a .env file

# Initialize Hugging Face Inference Client
client = InferenceClient(
    provider="hf-inference",
    api_key=API_KEY,
)

# Streamlit UI Setup
st.set_page_config(page_title="Mistral-7B Chatbot", layout="centered")
st.title("🤖 Mistral-7B Chatbot")

# Chat message history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
user_input = st.chat_input("Type your message...")
if user_input:
    # Append user message
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)
    
    # API request to Mistral-7B
    with st.spinner("Thinking..."):
        try:
            completion = client.chat.completions.create(
                model="mistralai/Mistral-7B-Instruct-v0.1",
                messages=st.session_state["messages"],
                max_tokens=500,
            )
            response = completion.choices[0].message["content"]
        except Exception as e:
            response = f"Error: {str(e)}"
    
    # Append bot response
    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
