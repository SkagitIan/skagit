import streamlit as st
from transformers import pipeline
import tensor

# Initialize the chatbot pipeline
chatbot = pipeline('text-generation', model='microsoft/DialoGPT-medium')

st.title('Simple Chatbot')

# User input
user_input = st.text_input("You: ", "")

if st.button('Send'):
    if user_input:
        # Generate a response
        response = chatbot(user_input, max_length=50)
        st.text_area("Bot:", value=response[0]['generated_text'], height=200, max_chars=None, key=None)
    else:
        st.write("Please type a message.")
