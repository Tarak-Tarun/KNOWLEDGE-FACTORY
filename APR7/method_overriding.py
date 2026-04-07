class Shape:
    def area(self):
        print("Area not defined for Shape Objects")


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

sh=Shape()
sh.area()
s = Square(4)
r = Rectangle(5, 3)

print("Square Area:", s.area())
print("Rectangle Area:", r.area())