# Air India Express FAQ Chatbot

## Overview
The Air India Express FAQ Chatbot is a conversational interface designed to assist users by providing instant answers to frequently asked questions related to Air India Express services. This project utilizes machine learning techniques, specifically TF-IDF and cosine similarity, to match user queries with predefined FAQ data.

## Features
- **Interactive Chat Interface**: Users can either ask custom questions or select from a list of predefined FAQs.
- **Natural Language Processing**: The chatbot utilizes TF-IDF vectorization to understand and respond to user queries effectively.
- **Conversation History**: Keeps track of the chat history, allowing users to see previous interactions.
- **Customizable FAQ Data**: The bot can be trained with different FAQ datasets as needed.

## Technologies Used
- **Python**: The primary programming language for building the chatbot.
- **Streamlit**: A powerful library for creating web applications in Python, used for the chatbot interface.
- **Scikit-learn**: For implementing the TF-IDF vectorizer and cosine similarity calculations.
- **Requests**: For fetching FAQ data from an external source.

## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/air-india-express-faq-chatbot.git
   cd air-india-express-faq-chatbot
## Installation

To install the required packages, run the following command:

```
pip install -r requirements.txt
```

## Usage

To run the application, use the following command:

```
streamlit run app.py
```

After running the command, open your web browser and navigate to [http://localhost:8501](http://localhost:8501) to interact with the chatbot.
