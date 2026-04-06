class Car:
    def __init__(self, brand, model, features):
        self.brand = brand
        self.model = model
        self.features = features
    def __str__(self):
        return f"{self.brand} {self.model}"
    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}', {self.features})"

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return self.brand == other.brand and self.model == other.model

    def __len__(self):
        return len(self.features)
car1 = Car("Hyundai", "Creta", ["AC", "Airbags", "Sunroof"])
car2 = Car("Hyundai", "Creta", ["AC", "Airbags"])
car3 = Car("Toyota", "Fortuner", ["AC", "4x4"])
print("Using print():", car1)
print("Using repr():", repr(car1))
print("car1 == car2:", car1 == car2)
print("car1 == car3:", car1 == car3)
print("Number of features in car1:", len(car1))
print("List view:", [car1, car2, car3])