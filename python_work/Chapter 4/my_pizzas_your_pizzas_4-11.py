pizzas = ['ananas','salami','classic']
friend_pizzas = pizzas[:]
pizzas.append('kabanosy')
friend_pizzas.append('piwowa')

print("\nMy favorite pizzas are:")

for pizza in pizzas: print(pizza.title())

print("\nMy friend's favorite pizzas are:")

for pizza in friend_pizzas: print(pizza.title())