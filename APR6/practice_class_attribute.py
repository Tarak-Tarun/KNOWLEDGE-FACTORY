class Employee:
    employee_count=0
    def __init__(self,employee):
        self.employee=employee
        print(f"Object for Employee {self.employee} Created")
        Employee.employee_count+=1
    @classmethod
    def number_of_employees(cls):
        print(f"Number of Employees: {cls.employee_count}")
Tarak=Employee("Tarak Tarun")
Employee.number_of_employees()
Bharath=Employee("Bharath Kumar")
Employee.number_of_employees()
Shaalim=Employee("Shaalim Raj")
Employee.number_of_employees()
Lokesh=Employee("Lokesh Vasu Dev")
Employee.number_of_employees()

