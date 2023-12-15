places = ["Paris","Miami","Gdansk","Machu-Pikchu","Australia"]

print(f"Places I would like to visit: {places}")
print(f"Places sorted {sorted(places)}")
print(f"Original order after sorted: {places}")

places.reverse()

print(f"List reversed: {places}")

places.reverse()

print(f"List reversed again: {places}")

places.sort()

print(f"List sorted: {places}")

places.sort(reverse=True)

print(f"List sort(reverse=True): {places}")