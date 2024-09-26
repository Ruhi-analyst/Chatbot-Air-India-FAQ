import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you?", "Hi there!", "Hey, what's up?"]],
    [r"my name is (.*)", ["Hello %1, how are you today?"]],
    [r"how are you?", ["I'm just a bot, but I'm doing well!"]],
    [r"what is your name?", ["I am a chatbot created to assist you."]],
    [r"sorry (.*)", ["No problem at all!", "It's okay, no worries!"]],
    [r"im good", ["Good to know that, it's an honour you came here."]],
    [r"bye|goodbye", ["Goodbye! Have a nice day.", "See you later!"]],
    [r"(.*)", ["Sorry, I didn't understand that."]]  # Keep this as the last fallback option.
]

def chatbot():
    print("Hi, I am a simple chatbot. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
