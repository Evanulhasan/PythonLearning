# Function Arguments in Python 


# def average(a =9, b =1): # default Arguments 
#     avg = (a+b)/2
#     print(f"Average of {a} and {b} is {avg:.2f}")

# # average(10, 20)
# # average(5, 15)       # Required Arguments 
# average()



# def average(a =9, b =11): # default Arguments 
#     avg = (a+b)/2
#     print(f"Average of {a} and {b} is {avg:.2f}")

# average(19)
# average(5, 15)  
# average(b=9)

# def name(fname, mname = "Jhon", lname ="Whatson"):
#     print("Hello,", fname, mname, lname)

# name("Amy")
# name("Evanul", "Hasan", "Oualid")

# Key word agrument 



# def average(a =9, b =1,): # default Arguments 
#     avg = (a+b)/2
#     print(f"Average of {a} and {b} is {avg:.2f}")

# average(10, 20)
# average(5, 15)       # Required Arguments 
# average()            # Default Argument \
# average(b=18, a= 72) # Keyword agruments 


# Verible length argument 

def average(*numbers):
    print(type(numbers))
    if not numbers:
        return 0 
    sum = 0
    for i in numbers:
        sum +=  i 
    return sum/len(numbers)

print(average(5,6,7,8,4,9,19,33,44,645,45,54)) # Varible-length Argument 
c = average(53,44,33,43,7,25)
print(c)


def name(**name):
    print(type(name))
    print("Hello", name["fname"], name["mname"],name["lname"])


name(mname = "Buchanan", lname ="Barnes", fname="James")











