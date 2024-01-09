import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hi there!', 'Hello!', 'Hey!']),
    (r'how are you', ['I am good, thank you!', 'I\'m doing well, how about you?']),
    (r'quit', ['Bye!', 'Goodbye!', 'Take care!']),
    # Add more patterns and responses based on your requirements
]

# Create a chatbot using the defined patterns
chatbot = Chat(patterns, reflections)

# Function to start the chat
def start_chat():
    print("Hello! I'm your chatbot. You can type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

# Initialize the chat
start_chat()
