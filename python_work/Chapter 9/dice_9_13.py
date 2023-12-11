from random import randint

class Die:
    """Class to roll dice"""

    def __init__(self, sides = 6):
        """"""
        self.sides = sides

    def roll_die(self):
        """Method to roll dice"""
        for roll in range(0,10):
            print(f"Diece rolled: {randint(1, self.sides)}")

print('\n')
new_roll_1 = Die()
new_roll_1.roll_die()
print('\n')

new_roll_2 = Die(sides=10)
new_roll_2.roll_die()
print('\n')

new_roll_3 = Die(sides=20)
new_roll_3.roll_die()