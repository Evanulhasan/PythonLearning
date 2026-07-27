# Exercise 4 : Secret Code Language 

user_input = input("Enter the string: ")

if len(user_input)>3:
    a = user_input.removeprefix(user_input[0:1])
    b = a + user_input[0] + "asd"
    print(b)
    
else:
    user_input = user_input[-1::-1]
    print(user_input)
    





































