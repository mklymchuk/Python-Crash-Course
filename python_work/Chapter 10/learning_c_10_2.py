learning_python = '/Users/kola/VSCode/Python-Crash-Course/python_work/Chapter 10/learning_python.txt'

with open(learning_python) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip().replace('Python','C'))