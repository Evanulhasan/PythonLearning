# Inheritance in Python 
"""Inheritance is a core concept in object-oriented 
programming that allows a new class (child/derived class)
to adopt the attributes and methods of an existing class
(parent/base class). """

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id 
        
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Dipertment(Employee):
    def showDipertment(self):
        print(f"{self.id} is From IT Department")

class Programmer(Dipertment):
    def showLanguage(self):
        print(f"{self.name} is a Python Programmer. ")



e1 = Programmer("Evanul", 74)
e1.showDetails()
e1.showDipertment()
e1.showLanguage()
print("\n")

e2 = Programmer("Tanvir", 48)
e2.showDetails()
e2.showDipertment()
e2.showLanguage()
































