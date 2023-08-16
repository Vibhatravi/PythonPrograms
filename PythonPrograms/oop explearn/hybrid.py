# Creating a Base class named University:
class University:
    def __init__(self):
        self.univ = ""

    def take_input(self):
        self.univ = input("Enter the university name: ")

    def display(self):  
        print(f"The University name is: {self.univ}")

class Course(University):
    def __init__(self):
        super().__init__() 
        self.course = ""

    def take_input(self):
        self.course = input("Enter the course name: ")
        super().take_input()

    def display(self):  
        print(f"The Course name is: {self.course}")
        super().display()  

class Branch(University):
    def __init__(self):
        self.branch = ""

    def take_input(self):
        self.branch = input("Enter the branch name: ")

    def display(self): 
       raise print(f"The Branch name is: {self.branch}")

class Student(Course, Branch):
    def __init__(self):
        self.name = ""
        Course().__init__() 
        Branch().__init__() 

    def take_input(self):
        self.name = input("Enter the student name: ")
        Course().take_input()
        Branch().take_input()

    def display(self):
        print(f"The Name of the student is: {self.name}")
        Course().display()
        Branch().display() 

# Object Instantiation:
ob = Student()  
print()
ob.take_input() 
print()
ob.display()   
