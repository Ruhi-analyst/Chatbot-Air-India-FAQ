import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import json

# URL of the file containing FAQ data
url = 'https://storage.googleapis.com/kagglesdsdata/datasets/707597/1235002/faq_results.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240925%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240925T074953Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=3d80e1aa8b99fd65f83ec389b1febb0c27c72d6c2b1fb532f60bc0f64d429aaf83019b1d27f92179a13524015b1cf83126833c0d1e66de3dd00dd6183d15d196ce042d3062e0b64349da00c1c6dc2ddf1b412c7846f4b6fc5f7db598ec5cc1580508500a664875a650ea0e07e162746c07acf9fbf51f738fbc25a79ebc159f35d9d664a886b7dc7be7c00693ad003c0e463de5ebca9042f868869c8395d0a98b3d8c9cd303f54340fffcf9703b888279bd54f051302962b9d37d8284d6865ca394ab55dd03e7d4c5bf7f6cff0de9d0bec1e0fd648a489969a2f244251935dc7cfcc5791bef97e80c73db1aca5ea25542216513cb7451f12186599fe776aa47b5'

# Function to fetch data from the URL
def fetch_faq_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            # Load JSON data
            faq_data = json.loads(response.text)  # Expecting JSON format
            st.success("FAQ data loaded successfully!")
            return faq_data
        except Exception as e:
            st.error(f"Error processing FAQ data: {e}")
            return None
    else:
        st.error(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Preprocess FAQ data by extracting questions and answers
def preprocess_faq_data(faq_data):
    try:
        questions = [item['Question'] for item in faq_data]  # Adjusted to extract from JSON
        answers = [item['Answer'] for item in faq_data]      # Adjusted to extract from JSON
        return questions, answers
    except KeyError as e:
        st.error(f"Data format error: {e}")
        return None, None

# Function to get the best matching answer based on user input
def get_response(user_input, vectorizer, tfidf_matrix, answers):
    user_input_tfidf = vectorizer.transform([user_input])
    similarity_scores = cosine_similarity(user_input_tfidf, tfidf_matrix)
    
    best_match_index = similarity_scores.argmax()
    return answers[best_match_index]

# Streamlit UI
st.title("🤖 Custom FAQ Chatbot")
st.markdown("""
Welcome to the **FAQ Chatbot**! 
Click on any question below to get an instant response or type in your custom question.
""")

# Load the FAQ data
faq_data = fetch_faq_data(url)

if faq_data:
    questions, answers = preprocess_faq_data(faq_data)

    # Display clickable pre-made questions
    st.subheader("Pre-Made Questions:")
    for q, a in zip(questions, answers):
        if st.button(q):  # Create a button for each pre-made question
            st.markdown(f"<div class='bot-message'>**Answer:** {a}</div>", unsafe_allow_html=True)  # Display the answer when the button is clicked

    if questions and answers:
        # TF-IDF vectorizer to transform the FAQ questions
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(questions)

        # Initialize session state to keep track of conversation history
        if 'conversation_history' not in st.session_state:
            st.session_state.conversation_history = []

        # Input box for user question
        st.subheader("Ask a Custom Question:")
        user_input = st.text_input("Your Question", placeholder="Type here...", key="user_input")

        # Button to send the custom question
        if st.button("Send") or (st.session_state.get("send", False) and user_input):
            response = get_response(user_input, vectorizer, tfidf_matrix, answers)
            st.markdown(f"<div class='user-message'>**You:** {user_input}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='bot-message'>**Answer:** {response}</div>", unsafe_allow_html=True)

            # Save the user question and the response to the conversation history
            st.session_state.conversation_history.append((user_input, response))
            st.session_state.send = False  # Reset after sending
        else:
            st.session_state.send = True  # Set send to true for Enter key

        # Display conversation history
        if st.session_state.conversation_history:
            st.subheader("Conversation History:")
            for q, a in st.session_state.conversation_history:
                st.markdown(f"<div class='user-message'>**You:** {q}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='bot-message'>**Bot:** {a}</div>", unsafe_allow_html=True)

    else:
        st.warning("No valid questions and answers found. Please check the data format.")
else:
    st.error("Failed to load FAQ data.")

# Footer with some extra chatbot instructions or branding
st.markdown("""
💡 **Tip**: The chatbot can only answer based on the data it has been trained on. Ask concise, specific questions!
""")

# Add custom CSS to style the buttons and messages
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f0f4f8; /* Light Gray Background */
            color: #333;
        }
        .stButton > button {
            background-color: #5a67d8;  /* Blue */
            color: white;
            padding: 10px 24px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 10px;
            transition: background-color 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #434190;  /* Darker Blue */
        }
        .user-message {
            background-color: #007bff;  /* Strong Blue */
            color: white;  /* White text for contrast */
            border: 1px solid #0056b3; /* Darker Blue Border */
            padding: 12px;
            border-radius: 10px;
            margin: 5px 0;
            display: inline-block;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            max-width: 70%;
            position: relative;
        }
        .bot-message {
            background-color: #28a745;  /* Strong Green */
            color: white;  /* White text for contrast */
            border: 1px solid #218838; /* Darker Green Border */
            padding: 12px;
            border-radius: 10px;
            margin: 5px 0;
            display: inline-block;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            max-width: 70%;
            position: relative;
        }
        .stTextInput > div > input {
            border-radius: 4px;
            border: 1px solid #ccc;
            padding: 10px;
            width: 100%;
            margin-top: 10px;
        }
        .stTextInput > div > input:focus {
            border-color: #5a67d8;  /* Focus border color */
            outline: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Add JavaScript to enable Enter key functionality
st.markdown(
    """
    <script>
    const inputField = document.querySelector('input[type="text"]');
    const sendButton = document.querySelector('button[title="Send"]');
    
    inputField.addEventListener('keypress', function(event) {
        if (event.key === "Enter") {
            event.preventDefault(); // Prevent the default action
            sendButton.click(); // Simulate button click
        }
    });
    </script>
    """,
    unsafe_allow_html=True
)
