class A:
    def show(self):
        print("Method from A")

class B(A):
    pass   

class C(A):
    pass   

class D(B, C):
    pass


obj = D()

obj.show()

# Print MRO
print(D.mro())