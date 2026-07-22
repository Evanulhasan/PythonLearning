# Recursion in python 

# factorial(7) = 7*6*5*4*3*2*1 
# factorial(6) = 6*5*4*3*2*1 
# factorial(7) = 5*4*3*2*1 
# factorial(7) = 4*3*2*1 
# factorial(0) = 1 


# factorial(n) = n * factorial(n-1)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)



# print(factorial(3))
# print(factorial(4))
# print(factorial(5))
# print(factorial(6))

# Fibonacci Calculator  using recartion 
def febo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return febo(n-1) + febo(n-2) 


a = int(input("Entr the number: "))
print(febo(a))



# def get_nth_fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
        
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b

# # Example usage:
# print(get_nth_fibonacci(40))
# # Output: 55











































