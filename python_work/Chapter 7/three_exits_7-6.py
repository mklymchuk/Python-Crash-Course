prompt = "\nPlese, enter pizza topping: "
prompt += "\n(Enter 'quit' to exit)\n"

active = True

toppings = []

while active:
    message = input(prompt)
    
    if message == 'quit':
        break
    else:
        toppings.append(message)
        print("You'll add that topping to their pizza: " + message.capitalize())
        
print("Added toppings: ", toppings)
    