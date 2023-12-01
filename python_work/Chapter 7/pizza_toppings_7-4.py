prompt = "\nPlese, enter pizza topping: "
prompt += "\n(Enter 'quit' to exit)\n"

active = True

while active:
    message = input(prompt)
    
    if message == 'quit':
        break
    else:
        print("You'll add that topping to their pizza: " + message.capitalize())