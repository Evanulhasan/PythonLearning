#  How import work in Python 
# Importing in Pyhon is the process of loading 
# code from a Python module into the current Script.


# import pandas 
# print(pandas.__version__)
# pandas.read_csv()

## Importing  math module in Python
# import math 
# print(math.sqrt(16))
# print(math.floor(4.4545))

# #Importing specific functions from a module
# from math import sqrt,pi 
# print(sqrt(20))
# print(pi)

# Importing all functions from a module
# from math import sqrt, pi, floor, ceil, log, pow as math_pow
# print(sqrt(25))
# print(pi)
# print(floor(4.4545))
# print(ceil(4.4545))
# print(log(10))
# print(math_pow(2, 3))

# # Importing a module with an alias "as"
# import math as m
# print(m.sqrt(9)*m.pi)
# print(m.pi)
# print(m.floor(4.4545))


# # This will show all the attributes and methods of 
# # the math module   
# import math
# print(dir(math))  

# print(math.nan, type(math.nan))

# #  # This will show the documentation of the math module
# # print(help(math)) 

# print(math.isclose(0.1 + 0.2, 0.3))  # True


# import oualid 

## Importing a module in Python
# print(dir(oualid))
# oualid.welcome()
# print(oualid.oualid)

# Importing specific functions and variables from a module
from oualid import welcome, oualid
welcome()
print(oualid)






