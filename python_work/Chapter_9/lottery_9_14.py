from random import choices
"""Lottery"""

lottery = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'kola', 'dima', 'vika', 'kit', 'pes')

print("Any ticket matching these four numbers or letters win a prize.")

for i in range(4):
    print(choices(lottery))