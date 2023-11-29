mykola_person = {'first_name':'Mykola',
                 'last_name':'Klymchuk',
                 'age':28,
                 'city':'Ivano-Frankivsk'}

viktoria_person = {'first_name':'Viktoria',
                 'last_name':'Klymchuk',
                 'age':16,
                 'city':'Ivano-Frankivsk'}

dima_person = {'first_name':'Dmytro',
                 'last_name':'Klymchuk',
                 'age':27,
                 'city':'Ivano-Frankivsk'}

people = [mykola_person,viktoria_person,dima_person]

for peoples in people:
    print("\n")
    for person in peoples:
        print(f"{person} : {peoples[person]}")