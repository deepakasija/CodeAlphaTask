#task 3
import nltk
from nltk.chat.util import Chat, reflections

# Define some basic patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am good, thank you!', 'I\'m fine, thanks. How about you?']),
    (r'(.*) your name', ['I am a chatbot. You can call me ChatGPT!', 'I don\'t have a name, but you can call me Chatbot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    # Add more patterns and responses as needed
]

# Create a chatbot using NLTK's Chat class
chatbot = Chat(patterns, reflections)

# Function to start and run the chatbot
def run_chatbot():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Goodbye! Have a great day.")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

# Download NLTK data (only need to do this once)
nltk.download('punkt')

# Run the chatbot
run_chatbot()
