equal_string = 'america'
basic_string = 'cocacola'
basic_string_1 = 'Cocacola'
numbers = [numbers for numbers in range(1,11)]

print("Equal and non equal string test")
print(f"Equal string 'america", equal_string == 'america')
print(f"Non equal string 'america'", equal_string != 'america')
print("Is cocacola and Cocacola the same in python?")
print(f"cocacola", basic_string == 'cocacola')
print(f"Cocacola", basic_string == 'Cocacola')
print(f"Cocacola with lower() method", basic_string == basic_string_1.lower())
print("\nNumerical tests: == , != , > , < , >= , <= :")
print(f"list 1-10 == 0", numbers == 0)
print(f"list 1-10 != 0", numbers == 0)
print(f"sum of list 1-10 < 100", sum(numbers) < 100)
print(f"sum of list 1-10 > 100", sum(numbers) > 100)
print(f"sum of list 1-10 <= 55", sum(numbers) <= 55)
print(f"sum of list 1-10 >= 54", sum(numbers) >= 54)
print(f"Test with 'and' and 'or' keywords: ")

if numbers[1+2] and numbers[0+3] == 4:
    (print("'and' equal"))
else:
    print("not equal")

if numbers[1+2] or numbers[0+4] == 4:
    print("'or' equal")

print("\nTest is iteam in list: ")

number = 1

print(number in numbers)
print("\nTest is iteam not in a list: ")