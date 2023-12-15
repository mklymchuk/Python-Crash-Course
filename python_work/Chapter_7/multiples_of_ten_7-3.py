ask_for_a_number = "Please, enter the number: "
user_input = input(ask_for_a_number)
user_input = int(user_input)
if user_input % 10 == 0:
    print("Number is multiple of 10")
else:
    print("Number is not multiple of ten")