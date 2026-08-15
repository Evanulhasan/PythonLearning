# Access Modifiers in Python 
# Public Access Modifier
# class Employee:
#     def __init__(self):
#         self.name = "Evanul"

# a = Employee()
# print(a.name)



# # Private Access Modifier 
# class Employee:
#     def __init__(self):
#         self.__name = "Evanul"

# a = Employee()
# # print(a.__name) # Can not access Directly 
# print(a._Employee__name) # Can be access In-Directly
# # It's call Name Mangling   



# Protected Access Modifier 
class Student:
    def __init__(self):
            self._name = "Evanul"
    
    def _nickName(self):
        return "Oualid"

class Department(Student):
    pass


obj = Student()
obj1 = Department()


print(obj._name)
print(obj._nickName())

# print(obj.__dir__())
print(dir(obj))

print(obj1._name)
print(obj1._nickName())




























































