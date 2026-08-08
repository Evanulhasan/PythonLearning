# Map, Filter and Reduce in Python 

# l = [1, 2, 3, 4, 5]
# newl = []
# for i in l:
#     newl.append(i * i * i)

# print(newl)

# 
# def cube(numbers):
#     cubl = []
#     for num in numbers:
#         cubl.append(num * num * num)
#     return cubl
    

# mylist = [1, 2, 3, 4, 5]
# result = cube(mylist)

# print(result)


# Map in python 
# def cube(x):
#     return x * x * x 

# l = [1, 2, 3, 4, 5]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))
# newl = list(map(cube, l))
# print(newl)


# # Lambda 
# l = [1, 2, 3, 4, 5]
# newl = list(map(lambda l: l * l * l, l))
# print(newl)


# Filter in Python 


# def cube(x):
#     return x * x * x 

# l = [1, 2, 3, 4, 5, 7, 8, 11]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))
# newl = list(map(cube, l))
# print(newl)


# def filter_function(a):
#     return a>3

# newll = list(filter(filter_function, l))
# print(newll)


# Reduce in Python
from functools import reduce 


# List of numbers 
numbers = [1, 2, 3, 4, 5, 6]

def mysum(x, y):
    return x  + y
    
sum = reduce(mysum, numbers)

print(sum)


















