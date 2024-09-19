def chatbot_response(user_input):
    user_input = user_input.lower()

    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I help you today?"

    elif 'bye' in user_input:
        return "Goodbye! Have a nice day!"

    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm doing great! Thanks for asking."

    elif 'name' in user_input:
        return "I am your simple chatbot!"

    else:
        return "Sorry, I didn't understand that. Can you please ask something else?"

print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! Have a great day!")
        break
    else:
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
