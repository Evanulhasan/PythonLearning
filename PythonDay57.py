# Classes and Objects in Python 

class Person:
    name = "Evanul Hasan Oualid"
    occupation = "Software Developer"
    networth = 10 
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a = Person()
a.name = "Tanvir"
a.occupation = "Accountant"
print(a.name, a.occupation)
a.info()

b = Person()
b.name = "Usman"
b.occupation = "HR"
b.info()








































