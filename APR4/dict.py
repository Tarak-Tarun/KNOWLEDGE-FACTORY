d = {1: 10, 2: 20, 3: 30}

print("Dictionary:", d)

print("Get value:", d.get(2))
print("Get missing key:", d.get(5, "Not Found"))

print("Keys:", d.keys())
print("Items:", d.items())

d2 = {x: x*x for x in range(1, 5)}
print("Comprehension:", d2)