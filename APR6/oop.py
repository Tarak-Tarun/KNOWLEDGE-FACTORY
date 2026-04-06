class Design:
    def __init__(self):
        print("Object Created")
    def color(self, colour):
        self.colour = colour
        print(f"Design Color : {self.colour}")
    def wheels(self, wheel_type):
        self.wheel_type = wheel_type
        print(f"Wheel Type: {self.wheel_type}")

    def mode(self, riding_mode):
        self.riding_mode = riding_mode
        print(f"Riding Mode: {self.riding_mode}")
obj = Design()
obj.color("Red")
obj.wheels("Alloy")
obj.mode("Eco Saving")