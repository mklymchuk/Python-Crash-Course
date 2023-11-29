lion_cat = {'kind_of_animal':'cat',
            'owner_name':'Mykola',}

mad_dog = {'kind_of_animal':'dog',
            'owner_name':'Viktoria',}

crazy_chiken = {'kind_of_animal':'chicken',
            'owner_name':'Dmytro',}

pets = [lion_cat,mad_dog,crazy_chiken]

for pet in pets:
    print("\n")
    for key, value in pet.items():
        print(f"{key} : {value}")