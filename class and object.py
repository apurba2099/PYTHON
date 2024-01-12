class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
    def calculate_salary(self):
       pass
    def print_employee_details(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Department:", self.department)
employee1 = Employee("Alice", 30, "Marketing")
employee2 = Employee("Bob", 25, "Sales")
print(employee1.name)  # Output: Alice
employee2.calculate_salary()
employee2.print_employee_details()
