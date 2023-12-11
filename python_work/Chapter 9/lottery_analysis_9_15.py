from random import randint

my_ticket = [1, 2, 3, 5, 9]
lottery_flag = True
iterator = 0

def winning_ticket_rand():
    """Fill ticket with random numbers"""
    winning_ticket = []
    for _ in range(5):
        winning_number = randint(0, 10)
        winning_ticket.append(winning_number)
    return winning_ticket

def check_winning_ticket(my_ticket, winning_ticket):
    """Check number of my ticket, and winning ticket, and how many attempts
    needed to win"""
    if winning_ticket == my_ticket:
        print("You won!")
        return False
    else:
        print(f"Attempt to win: {iterator}")
        return True

while lottery_flag:
    iterator += 1

    winning_ticket = winning_ticket_rand()

    print(winning_ticket)

    lottery_flag = check_winning_ticket(my_ticket, winning_ticket)