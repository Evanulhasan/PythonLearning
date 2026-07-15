# Function in Python

# Geometric Mean 
def calculate_gmean(a, b):
    gmean = (a*b)/(a+b)
    print(f"Geometric Mean of {a} and {b} is {gmean:.2f}")

def isGreater(a, b):
    if a>b:
        print(f"{a} is greater than {b}")
    elif a<b:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} and {b} are equal")  

def islessThan(a, b):
    pass

a = 9 
b = 88
calculate_gmean(a, b)
isGreater(a, b)
c = 8
d = 78
calculate_gmean(c, d)
isGreater(c, d)
# gmean = (a*b)/(a+b)
# print(f"Geometric Mean of {a} and {b} is {gmean:.2f}")


























