import re

patterns_responses = {
    r'hi|hello|hey': 'Hello!',
    r'how are you bro': 'I am doing well bro, thank you!',
    r'my name is neal your name|what is your name': 'I am a chatbot programmed to assist you.',
    r'bye|goodbye': 'Goodbye! Have a great day!',
}

def generate_response(user_input):
    for pattern, response in patterns_responses.items():
        if re.search(pattern, user_input.lower()):
            return response
    return "I'm sorry, I don't understand that."

def main():
    print("Welcome to the chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        else:
            response = generate_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()