guests = ['Kernel Sanders','Ronald McDonald','Harry Potter']

print(f"Mr {guests[1]} cant be present on dinner")
guests.remove('Ronald McDonald')

guests.append('Sokrates')
for i in range(0,len(guests)):
    print(f"Dear mr {guests[i]}, I would like to invate you to dinner at 19:00")

print("Dear guests, we have bigger table")

guests.insert(0,'Mr Obama')
guests.insert(2,"McRee")
guests.append('John Xina')

for i in range(0,len(guests)):
    print(f"Dear mr {guests[i]}, I would like to invate you to dinner at 19:00")