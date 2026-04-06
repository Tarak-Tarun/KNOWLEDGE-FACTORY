class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self._price = price
        self._stock = stock
        self._discount = 0   

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @property
    def stock(self):
        return self._stock

    def add_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Cannot add negative stock")
        self._stock += quantity

    def reduce_stock(self, quantity):
        if quantity > self._stock:
            raise ValueError("Not enough stock")
        self._stock -= quantity

    def apply_discount(self, percent):
        if not (0 <= percent <= 100):
            raise ValueError("Discount must be between 0 and 100")
        self._discount = percent
    @property
    def final_price(self):
        return self._price * (1 - self._discount / 100)

    @property
    def info(self):
        return {
            "name": self.name,
            "price": self._price,
            "discount": self._discount,
            "final_price": self.final_price,
            "stock": self._stock
        }
p = Product("Laptop", 50000, 10)

print(p.info)

p.apply_discount(10)
print(p.final_price)

p.reduce_stock(2)
print(p.stock)