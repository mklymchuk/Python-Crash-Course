rivers = {'nile':'egypt','amazonka':'brazil','dnipro':'ukraine',}

for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print('\n')

for river in rivers.keys():
    print(f"Name of river - {river.title()}.")

print('\n')

for country in rivers.values():
    print(f"Name of country is - {country.title()}")