def show_messages(messages):
    print("\nFollowing messages in the list: ")
    for message in messages:
        print(message)
        
def send_messages(messages, sent_messages):
    print("\nThe following messages have bin sent: ")
    while messages:
        current_message = messages.pop()
        print(f"Message: {current_message}")
        sent_messages.append(current_message) 

short_messages = ['short message 1', 'short message 2', 'short message 3']
sent_messages = []

send_messages(short_messages[:], sent_messages) 
show_messages(sent_messages)       
