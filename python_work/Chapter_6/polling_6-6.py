favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

list_of_people = ['jen','sarah','olek','walter']

for person in list_of_people:
    if person in favorite_languages:
        print(f"Thank you for responding {person.title()}.")
    elif person not in favorite_languages:
        print(f"{person.title()} please take poll.")