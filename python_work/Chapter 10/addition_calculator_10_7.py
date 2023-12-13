"""Program add two numbers"""

def addition(number_one, number_two):
    """Addition of two numbers"""
    try:
        sum = int(number_one) + int(number_two)
    except ValueError:
        print("Please input two numbers")
    else:
        print(f"Sum of two numbers is: {sum}")

while True:
    print("If you want to quit, type 'q'")

    number_one = input("Please, type first number: ")

    if number_one == 'q':
        break

    number_two = input("Please, type second number: ")

    if number_two == 'q':
        break

    addition(number_one, number_two)