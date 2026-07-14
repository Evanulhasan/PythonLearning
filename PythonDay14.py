# If else Conditionals statements in Python 
# a = int(input("Enter your age:" ))
# print("Your age is:", a)

# # Conditional operators in Python
# #>, <, >=, <=, ==, !=

# print(a>18)
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# if(a>18):
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")


# applePrice = 130
# budget = 200 
# if(budget-applePrice > 100):
#     print("Alexa, add 3kg Apples to the cart")
# elif(budget-applePrice > 80):
#     print("Alexa, add 2kg Apples to the cart")
# elif(budget-applePrice > 50):
#     print("Alexa, add 1kg Apples to the cart")
# else:
#     print("Alexa, do not add Apple to the cart")



# num = int(input("Enter a number: "))

# if(num < 0):
#     print("The number is negative")
# elif(num == 0):
#     print("The number is zero")
# elif(num == 999):
#     print("The number is 999")
# else:
#     print("The number is positive")


# Nested if else statements in Python
# num = 18
# if(num < 0):
#     print("The number is negative")
# elif(num > 0):
#     if(num <= 10):
#         print("The number is positive and less than or equal to 10")
#     elif(num >10 and num <=20):
#         print("The number is positive and between 11 and 20")
#     else:
#         print("The number is positive and greater than 20")
# else:
#     print("The number is zero")


# Nested if else statements in Python 

num = int(input("Enter a number: "))
if(num < 0):
    print("The number is negative")
    if(num < -10):
        print("The number is less than -10")
    elif(num >= -10 and num < 0):
        print("The number is between -10 and 0")
elif(num == 0):
    print("The number is zero")
elif(num > 0):
    print("The number is positive")
    if(num > 10):
        print("The number is greater than 10")
    elif(num > 0 and num <= 10):
        print("The number is between 1 and 10")
else:
    print("Invalid input")



























