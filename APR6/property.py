class Product:
    def __init__(self,name,price):
        self.name=name
        self._price=price
    @property
    def show_data(self):
        return self.name,self._price
apple=Product("Apple",20)
print(apple.show_data)
apple.price=-10
print(apple.show_data)
