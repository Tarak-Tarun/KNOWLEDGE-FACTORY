class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __str__(self):
        return f"Product: {self.name},\n Price: {self.price}"
    def __repr__(self):
        return f"Product([{self.name},{self.price}])"
    def __eq__(self,other):
        if not isinstance(other,Product):
            return False
        return self.name==other.name and self.price==other.price

    def __len__(self):
        return len(self.name)
Laptop=Product("Laptop",70000)
Mobile=Product("Mobile",15000)
print(Laptop)
print(repr(Laptop))
print(Laptop==Mobile)
print(len(Laptop))