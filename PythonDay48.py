# Local Vs Global Variables in Python    

# Local variable is a variable that is defined inside a function and 
# can only be accessed within that function. A global variable is a 
# variable that is defined outside of any function and can be accessed 
# from anywhere in the code.

# x = 4 
# print(x) # This will print the global variable x which is 4


# def hello():
#     x = 5 # This is a local variable x which is defined inside the function hello()
#     print(f"The local variable x is, {x}")
#     print("Hello World") # This will print the global variable x which is 4 and then print "Hello World"



# print(f"The global variable x is, {x}")
# hello()
# print(f"The global variable x is, {x}") # This will print the global variable x which is 4




x = 10 # global variable x

def my_function():
    global x
    x = 4
    global y
    y = 5 # local variable y
    print(y)
    
my_function() # This will print the local variable y which is 5
print(x)
print(y) # This will give an error because y is a local variable and cannot be accessed outside the function
























































