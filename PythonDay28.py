# F-Strings in Python 

# String formatting in Python 
letter = "Hey my name is {1} and i am from {0}"
country = "India"
name = "Harry"
print(letter.format(country,name))

# f-string in python 

country = "India"
name = "Harry"
letter = f"Hey my name is {name} and i am from {country}"
print("\n",letter)


print("\n")

# String formating 
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49.099999999))
print("\n")

# f-string in python
price = 745.4547564
txt = f"For lnly {price:.2f} dollars!"
print(txt)
print(f"{2*30}")

print("\n")

print(f"Hey my name is {{name}} and i am from {{country}}")
# If we want to {} braket in string we have to use 
# double {{}} braket like this
# 



























