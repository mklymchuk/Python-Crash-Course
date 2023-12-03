responses = []

# Set a flag to indicate polling is active.
polling_active = True

while polling_active:
    response = input("If you could visit one place in the world, where would you go? \n")
    responses.append(response)
    
    #Find out if anyone else is going to take the poll.
    repeat = input("Whould you like to let another person respond? (yes/no)\n")
    if repeat == 'no':
        polling_active = False
    
# Polling is complete. Show the results.
print("\n---Poll Results---")
for response in responses:
    print(f"Result is {response}.")