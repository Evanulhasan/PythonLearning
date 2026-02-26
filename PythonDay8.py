# Simple Calculator Using python

print("**************** CALCULATOR *******************")
print("\n")

num1 = float(input("Enter the first number here: "))
num2 = float(input("Enter the Second number here: "))

print("Enter 1 for 'Addition'\nEnter 2 for 'Subtraction'\nEnter 3 for 'Multiplication'\nEnter 1 for 'division'\nEnter 5 for 'Exponentiation'\nEnter 6 for 'Floor division'\n")

Entered_Number = int(input("Choice a number from 1 to 6 : "))

if Entered_Number == 1:
    print(f"The Addition of {num1}+{num2} is: {num1+num2}")
elif Entered_Number == 2:
    print(f"The Subtraction of {num1}-{num2} is: {num1-num2}")
elif Entered_Number == 3:
    print(f"The Multiplication of {num1}*{num2} is: {num1*num2}")
elif Entered_Number == 4:
    print(f"The Division of {num1}/{num2} is: {num1/num2}")
elif Entered_Number == 5:
    print(f"The Exponentiation of {num1}**{num2} is: {num1**num2}")
elif Entered_Number == 6:
    print(f"The Floor Division of {num1}//{num2} is: {num1//num2}")
else:
   print("Invalid input")
      























