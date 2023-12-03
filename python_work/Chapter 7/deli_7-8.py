sandwich_orders = ['BLT','Turkey Club','Grilled Cheese','Reuben','Chicken Caesar Wrap']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
    
print("\nThe following sandwiches was made: \n")
for sandwich in finished_sandwiches:
    print(sandwich)