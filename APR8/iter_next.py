lst = [1,2,3,4]
it = iter(lst)

while True:
    try:
        print(next(it),end=" ")
    except StopIteration:
        break