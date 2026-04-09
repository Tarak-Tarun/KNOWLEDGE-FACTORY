def demo():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")

g = demo()

print(next(g))
print(next(g))

try:
    print(next(g))
except StopIteration:
    print("StopIteration")