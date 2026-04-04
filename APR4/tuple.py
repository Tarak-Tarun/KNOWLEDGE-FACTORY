t = (10, 20, 30)

print("Original:", t)

print("Access:", t[1])

t = t + (40,)
print("After adding:", t)

t = t[:1] + (25,) + t[2:]
print("After change:", t)