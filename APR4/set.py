a = {1, 2, 3}
b = {3, 4, 5}

print("Set A:", a)
print("Set B:", b)

a.add(6)
print("After adding to A:", a)

a.remove(2)
print("After removing from A:", a)

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (A - B):", a - b)
print("Difference (B - A):", b - a)