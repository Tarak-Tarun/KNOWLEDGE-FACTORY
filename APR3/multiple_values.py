def home():
    return 10,20,"30",40,50
print(home())
print(type(home()))


def even(n):
    array=[]
    for i in range(0,n+1):
        if i%2==0:
            array.append(i)
    return array
print(even(100))
