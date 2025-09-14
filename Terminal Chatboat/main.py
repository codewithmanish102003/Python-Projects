# chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I’m PyBot, your friendly chatbot 🤖"
    elif "how are you" in user_input:
        return "I’m doing great! Thanks for asking. How about you?"
    elif "help" in user_input:
        return "Sure! You can ask me about weather, time, or just say hi!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day 😊"
    else:
        return "I’m not sure I understand that. Can you rephrase?"

def start_chat():
    print("PyBot: Hi, I’m PyBot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("PyBot:", response)
        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    start_chat()