prompt = "Please, entere your age: "

active = True

while active:
    
    age = input(prompt)
    age = int(age)
    
    if age <= 3:
        print("Ticket is free")
    elif age > 3 and age <= 12:
        print("Ticket is 12$")
    else:
        print("Ticket is 15$")