class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def checkout(self):  
        print(f"Checking out {self.item} worth ₹{self.price}")


class OnlineOrder(Order):
    def __init__(self, item, price, address):
        super().__init__(item, price)
        self.address = address

    def delivery(self):
        print(f"Delivering to {self.address}")


class PickupOrder(Order):
    def __init__(self, item, price, store_location):
        super().__init__(item, price)
        self.store_location = store_location

    def pickup(self):
        print(f"Pickup from {self.store_location}")


online = OnlineOrder("Laptop", 50000, "Hyderabad")
pickup = PickupOrder("Shoes", 2000, "Store A")

online.checkout()
pickup.checkout()

online.delivery()
pickup.pickup()