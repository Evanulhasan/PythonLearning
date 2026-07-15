# Break and Continue Statement in Python


# for i in range(1, 13):
#     print(f"3 x {i} = {3*i}")
#     if i == 10:
#         break


# # break 
# for i in range(1, 13):
#     if i == 11:
#         break
#     print(f"3 x {i} = {3*i}")



# Continue Statement 
for i in range(1, 13):
    if i == 4:
        print("12 Skip")
        continue
        
    print(f"3 x {i} = {3*i}")


# for i in range(1, 101, 1):
#     print(i, end=" ")
#     if(i==50):
#         break 
#     else:
#         print("Mississippi")
# print("\nDone with the loop")



# Do While loop  emulation in Python 
# i = 0 
# while True:
#     print(i)
#     i = i + 1
#     if (i%100==0):
#         break

i = 1   
while True:
    print(i)  
    i = i + 1
    if(i>=1):
        break











