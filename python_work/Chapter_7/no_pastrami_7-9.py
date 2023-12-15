sandwich_orders = ['BLT','Pastrami','Turkey Club','Grilled Cheese','Pastrami','Reuben','Chicken Caesar Wrap','Pastrami']
finished_sandwiches = []

print("Deli has run out of Pastrami")

while sandwich_orders:
    
    if 'Pastrami' in sandwich_orders:
        sandwich_orders.remove('Pastrami')
        
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
    
print("\nThe following sandwiches was made: \n")
for sandwich in finished_sandwiches:
    print(sandwich)