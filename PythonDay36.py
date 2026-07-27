#Exception Handdling in Python    
# Exception handling is the porcesof responding to 
# unwanted or unexpected events when a computer program rens. 
# Exception handling deals with there events to 
# avoid the program of system carahing and without this process


# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#     for i in range(1, 11):
#         print(f"{int(a)} x {i} = {int(a)*i}")
    
# except:
#     print("Invalid Input!")  
    
    
# print("Some lines of code")
# print("End of program")


try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number Entered is not an Integer.")
except IndexError:
    print("Index Error")
































