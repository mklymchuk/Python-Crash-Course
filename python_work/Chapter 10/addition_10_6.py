"""Program add two numbers"""

number_one = input("Please, type first number: ")
number_two = input("Please, type second number: ")

try:
    sum = int(number_one) + int(number_two)
except ValueError:
    print("Please input two numbers")
else:
    print(f"Sum of two numbers is: {sum}")