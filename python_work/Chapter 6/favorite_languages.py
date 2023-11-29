favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python', 'haskell'],
}

language = favorite_languages['sarah']

print(f"Sarah's favorite language is {language}.")

for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages is are:")
    for language in languages:
        print(f"\t{language.title()}")

print('\n')

friends = ['phil', 'sarah']

for name, languages in favorite_languages.items():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = ', '.join(languages).title()
        print(f"\t{name.title()}, I see you love {language}!")


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the pool.")

print('\n')

print("The following languages have been mentioned:")
for language in set(language for languages in favorite_languages.values() for language in languages):
    print(language.title())