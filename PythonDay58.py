# Constructors in Python 
class Person:
    def __init__(self, n, o):
        print("Hey I am a Person.")
        self.name = n 
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}.")



a = Person("Evanul", "Developer")
b = Person("Divya", "HR")
c = Person()
a.info()
b.info()
# # print(a.name)
# a.name = "Shadin"
# a.occ = "HR"
# a.info()




























