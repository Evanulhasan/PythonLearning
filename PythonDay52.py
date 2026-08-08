# Lambda Functions in Python 


# def add(a, b):
#     """Add two numbers and return the result."""
#     return a + b

# print(sum(5, 10))  # Output: 15


def double(x):
    """Double the input value."""
    return x * 2
print(double(5))  # Output: 10

# Lambda function to double a number
lambda_double = lambda x: x * 2
print(lambda_double(10))  # Output: 20

# Lambda function to calculate the cube of a number   
cube = lambda x: x * x * x
print(cube(3))  # Output: 27


# x = 4
# y = 5
# z = 6 

# average = lambda x, y, z: (x + y + z) / len([x, y, z])
# print(len([x, y, z]))  # Output: 3
# print(average(x, y, z))  # Output: 5.0


def add(cube_func, value):
    """Add a value to the average."""
    return 100 + cube_func(value)


cube = lambda x: x * x * x

# cube_value = cube(4)  # Calculate the cube of 4

print(add(cube, 2))  # Output: 164.0













