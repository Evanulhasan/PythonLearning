# Raising Custom errors in Python 


# a = int(input("Enter any value between 5 and 9: "))

# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")


# quick quiz


user_input= input("Enter any value between 5 and 9: ")

if user_input == "quit":
    print("Program has been Executed")
else:
    try:
        num = int(user_input)
        if num>9 or num<5:
            raise ValueError("Value should be between 5 and 9")
        else:
            print(f"You entered {num}")
    except Exception as e:
        print("Ërror", e)
    finally:
        print("Evanul Hasan Oualid")































