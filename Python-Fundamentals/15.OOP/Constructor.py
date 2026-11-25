# A constructor is a special method that gets executed automatically when an object is created.

# In Python, we use:
# __init__()

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
e1=Employee("Sakshi",30000)
e1.display()

# __init__ is the special initialization method.
# self refers to the current object.
# name and salary receive values passed during object creation.

#imp:
# self represents the current object of a class.
# It allows us to access the attributes and methods belonging to that particular object.

# Important points about self
# 1. self is not a Python keyword.
# 2. We can technically use another parameter name, but self is the standard convention.
# 3. It must be the first parameter of a normal instance method.
# 4. It gives access to the current object's attributes and methods.
# 5. We don't pass self manually when calling an instance method through an object.
