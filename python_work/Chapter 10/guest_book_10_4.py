filename = 'guest_book.txt'
program_flag = True

def guest_record(guest_name):
    """Record of guest in .txt file"""
    with open(filename, 'a') as file_object:
        file_object.write(f"{guest_name} - visit record\n")

while program_flag:
    guest_name = input("Please, enter your name: ")

    if guest_name == 'q':
        program_flag = False
    else:
        print(f"Greatings, {guest_name}")
        guest_record(guest_name)
        print("Type 'q' if you want to quit program: ")