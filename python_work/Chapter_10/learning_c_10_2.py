learning_python = 'txt/learning_python.txt'

with open(learning_python) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip().replace('Python','C'))