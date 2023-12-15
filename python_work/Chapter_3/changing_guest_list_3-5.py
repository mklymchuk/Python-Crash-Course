guests = ['Kernel Sanders','Ronald McDonald','Harry Potter']

print(f"Mr {guests[1]} cant be present on dinner")
guests.remove('Ronald McDonald')

guests.append('Sokrates')
for i in range(0,len(guests)):
    print(f"Dear mr {guests[i]}, I would like to invate you to dinner at 19:00")
