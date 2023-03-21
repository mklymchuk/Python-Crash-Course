my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\nList of my foods: \n")

for food in my_foods: print(f"{food.title()}")

print("\nList of my friend foods:\n")

for food in friend_foods: print(f"{food.title()}")