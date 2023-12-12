#1
with open('/Users/kola/VSCode/Python-Crash-Course/python_work/Chapter 10/learning_python.txt') as file_object:
    contents = file_object.read()

print(contents)
print('\n')

#2
with open('/Users/kola/VSCode/Python-Crash-Course/python_work/Chapter 10/learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#3
with open('/Users/kola/VSCode/Python-Crash-Course/python_work/Chapter 10/learning_python.txt') as file_object:
    lines = file_object.readlines()

new_string = ''
for line in lines:
    new_string += line.rstrip()

print(new_string)