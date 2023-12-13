filename = 'txt/question_answers.txt'
program_flag = True

def question_answers(question_answer):
    """Record of what people like in programming in .txt file"""
    with open(filename, 'a') as file_object:
        file_object.write(f"{question_answer}\n")

while program_flag:
    question_answer = input("Why you like programming?\n")

    if question_answer == 'q':
        program_flag = False
    else:
        question_answers(question_answer)
        print("Type 'q' if you want to quit program: ")