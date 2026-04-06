class Car:
    wheels=4

    def __init__(self,model_name):
        self.model_name=model_name
        print("Object Created for ",model_name)
        print("Model Name: ",self.model_name)
        print("Number of Wheels for" ,model_name ," model : ", self.wheels)
    @classmethod
    def print_wheels(cls):
        print(f"Number of Wheels for all Models: {cls.wheels}")
    def model_color(self,color="White"):
        self.color=color
        print(f"{self.model_name} Color: {self.color}")
hyundai=Car("Hyundai")
Car.print_wheels()
hyundai.model_color("Black")

creta=Car("Creta")
Car.print_wheels()
creta.model_color()

    