import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

# Define the chatbot pairs
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you?", "Hi there!", "Hey, what's up?"]],
    [r"my name is (.*)", ["Hello %1, how are you today?"]],
    [r"how are you?", ["I'm just a bot, but I'm doing well!"]],
    [r"what is your name?", ["I am a chatbot created to assist you."]],
    [r"sorry (.*)", ["No problem at all!", "It's okay, no worries!"]],
    [r"im good", ["Good to know that, it's an honour you came here."]],
    [r"bye|goodbye", ["Goodbye! Have a nice day.", "See you later!"]],
    [r"(.*)", ["Sorry, I didn't understand that."]]
]

# Create the chatbot instance
chatbot = Chat(pairs, reflections)

# Streamlit UI code
st.title("Simple Chatbot")

# Text input field for the user message
user_input = st.text_input("You: ")

# When the user submits a message, generate a response
if user_input:
    response = chatbot.respond(user_input)
    st.text_area("Chatbot:", value=f"Bot: {response}", height=200, max_chars=None, key=None)

