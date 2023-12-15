languges = ['english','polish','ukrainian','japanese','spanish','hungry','macedonian']
message = "This is language - "

for i in range(0,len(languges)):
    print(message + languges[i].title())

print(f"This languge is fake: {languges[-2].title()}")

languges.remove('hungry')

print(f"so we remove it and this is our list now {languges}")

languges.append('korean')

print("Add language - 'korean'")
print("Also we inser as second and fourth language chinese and vietnamise")

languges.insert(1,'chinese')
languges.insert(3,'vietnamese')

for i in range(0,len(languges)):
    print(message + languges[i].title())

print(f"We need to delete language N5 and N6 {languges.pop(6).title(), languges.pop(7).title()}")
print(f"New list - {languges}")
print(f"List sorted() - {sorted(languges)}")
print(f"Original list - {languges}")

languges.reverse()

print(f"Languges reverse - {languges}")

languges.sort()

print(f"Languages sort() - {languges}")

languges.sort(reverse=True)

print(f"Languages sort(reverse=True) - {languges}")
print(f"List lenght have {len(languges)} languages")
print("\nList in the end:\n")

for i in range(0,len(languges)):
    print(message + languges[i].title())

for language in languges:
    print(message + language.title())