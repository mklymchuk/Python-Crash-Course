how_many_people = "How many people are in your dinner group? "
user_input = input(how_many_people)
user_input = int(user_input)

if user_input > 8:
    print("Sorry, but you need to wait for a table")
else:
    print("Your table is ready")