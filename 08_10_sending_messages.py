def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages):
    sent_messages = []  # List that holds sent messages
    while messages:
        message = messages.pop(0)  # Remove first message
        print(message)
        sent_messages.append(message)  # Add to sent_messages
    return sent_messages

# Short text messages list
text_messages = [
    "Hello, how are you?",
    "Don't forget our meeting tomorrow!",
    "Happy birthday!",
    "Congratulations on your achievement!",
    "Have a great day!"
]

# Call function to send messages
sent_messages = send_messages(text_messages)


print("\nText Messages:", text_messages)
print("Sent Messages:", sent_messages)