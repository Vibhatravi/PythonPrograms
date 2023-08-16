class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")


class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def manage_team(self):
        print(f"Managing the {self.department} department.")


class Developer(Employee):
    def __init__(self, name, employee_id, programming_language):
        super().__init__(name, employee_id)
        self.programming_language = programming_language

    def code(self):
        print(f"Coding in {self.programming_language}.")


# Getting employee details from the user
name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
department = input("Enter department: ")
programming_language = input("Enter programming language: ")

# Creating instances of Manager and Developer using user input
manager = Manager(name, employee_id, department)
developer = Developer(name, employee_id, programming_language)

# Calling methods from Person and Employee
manager.introduce()
manager.display_employee_info()

#developer.introduce()
developer.display_employee_info()

# Calling methods specific to Manager and Developer
manager.manage_team()
developer.code()
