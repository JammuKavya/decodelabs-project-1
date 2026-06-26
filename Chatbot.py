from datetime import datetime
responses={
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm functioning as expected! How about you?",
    "what is your name": "I am ChatBot, your virtual assistant.",
}
def show_help():
    print("""ailable commands:
    -hello
    -hi
    -how are you
    -what is your name
    -date
    -time
    -chathistory
    -help
    -exit""")
    
print("Welcome to the ChatBot! Type 'help' to see available commands.")
chat_history=[]
while True:
    user=input("\nYou:").strip().lower()
    chat_history.append(f"You: {user}")
    if user == "exit":
        print("ChatBot:Goodbye! Have a great day!")
        break
    elif user == "help":
        show_help()
    elif user =="date":
        current_date=datetime.now().strftime("%Y-%m-%d")
        print(f"ChatBot: Current date: {current_date}")
    elif user == "time":
        current_time=datetime.now().strftime("%H:%M:%S")
        print(f"ChatBot: Current time: {current_time}")
    elif user == "chathistory":
        print("ChatBot: Chat history:")
        for msg in chat_history:
            print(msg)
    else:
        response=responses.get(user)
        if response:
            print(f"ChatBot: {response}")
        else:
            print("ChatBot: I'm sorry, I didn't understand that. Please try again.")