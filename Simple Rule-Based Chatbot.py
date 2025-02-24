# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Rule 1: Greetings
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello! How can I assist you today?"

    # Rule 2: chatbot's name
    elif any(word in user_input for word in ["your name", "who are you"]):
        return "I am a simple rule-based chatbot. You can call me ChatBot!"

    # Rule 3: chatbot's status
    elif any(word in user_input for word in ["how are you", "how do you do"]):
        return "I'm just a program, so I don't have feelings, but thanks for asking!"

    # Rule 4: chatbot's capabilities
    elif any(word in user_input for word in ["what can you do", "help"]):
        return "I can respond to greetings, tell you my name, and answer simple questions. Try asking me something!"

    # Rule 5: Handle goodbye
    elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day!"

    # Rule 6: unknown inputs
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase or ask something else?"



def run_chatbot():
    print("Welcome to the Simple Rule-Based Chatbot!")
    print("You can start chatting. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")  
        if user_input.lower() in ["bye", "goodbye", "exit"]:
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)  
        print(f"ChatBot: {response}")



if __name__ == "__main__":
    run_chatbot()