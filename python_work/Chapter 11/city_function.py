"""Print a city name, and a country name"""

def city_country(city, country, population=''):
    """Print a city name, and a country name"""
    if population:
        city_country = f"{city.capitalize()}, {country.capitalize()} - population {population}"
    else:
        city_country = f"{city.capitalize()}, {country.capitalize()}"
    return city_country.title()