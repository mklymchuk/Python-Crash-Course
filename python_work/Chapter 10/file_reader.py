linux_file_path = '/home/mykola/Visual Studio Code/Python/Python Crash Course/python_work/Chapter 10/pi_digits.txt'
mac_file_path = '/Users/kola/VSCode/Python-Crash-Course/python_work/Chapter 10/pi_digits.txt'
filename = '/Users/kola/VSCode/Python-Crash-Course/python_work/Chapter 10/pi_million_digits.txt'

with open(mac_file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

print('\n')

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")