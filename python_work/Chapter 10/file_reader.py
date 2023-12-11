with open('/home/mykola/Visual Studio Code/Python/Python Crash Course/python_work/Chapter 10/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())