def chatbot():
    print("Chatbot: Hi! I am a simple chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "hi":
            print("Chatbot: Hello!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("Chatbot: I am a basic rule-based chatbot.")

        elif user_input == "who created you":
            print("Chatbot: I was created using Python.")

        elif user_input == "help":
            print("Chatbot: You can say hello, ask how I am, or type bye to exit.")

        elif user_input == "thank you":
            print("Chatbot: You're welcome!")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()
