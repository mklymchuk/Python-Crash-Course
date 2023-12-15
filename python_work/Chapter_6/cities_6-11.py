cities = {
    'Ivano-Frankivsk': {
        'country': 'Ukraine',
        'population': '300,000',
        'fact': '''Ivano-Frankivsk is a historic city located in western Ukraine.
                  It was initially known as Stanisławów and was part of the Austro-Hungarian Empire.'''
    },

    'Warsaw': {
        'country': 'Poland',
        'population': '3,000,000',
        'fact': '''Warsaw is the capital and largest city of Poland.
                  It has played a significant role in the country's history,
                  including being the site of the Warsaw Uprising during World War II.'''
    },

    'Wroclaw': {
        'country': 'Poland',
        'population': '500,000',
        'fact': '''Wrocław is often referred to as the "Venice of the North" due
                  to its numerous bridges and islands on the Oder River. The city has a
                  picturesque old town with a diverse architectural landscape.'''
    },
}
          
for city, city_info in cities.items():
    print(f"\nCity: {city}")
    print(f"country: {city_info['country']}")
    print(f"population: {city_info['population']}")
    print(f"fact about city: {city_info['fact']}")
    country = f"{'coutry'}"