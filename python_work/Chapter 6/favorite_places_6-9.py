favorite_places = {'dima':['dacha'],
                   'vika':['shkola','dim'],
                   'kola':['Ivano-Frankivsk','Wroclaw','Warszawa']
                   }

for name, place in favorite_places.items():
    name_capitalaize = name.capitalize()
    place = ', '.join(place)
    print(f"{name_capitalaize} : {place}")