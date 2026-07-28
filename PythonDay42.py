# Enumerate Function In Python 

marks = [12, 56, 32, 98, 12, 45, 1, 4]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Oualid, awesome!")
#     index +=1
        


# Enumerate Function is a built in function 
# in Python that allows you to loop over a 
# sequence and get the index an value of each 
# element in the squenct at the same time

# for index, mark in enumerate(marks,start = 1):
#     print(mark)
#     if(index == 3):
#         print("Oualid, awesome!")
    
        

name = "Evanul Hasan Oualid"

for index, i in enumerate(name, start = 1):
    print(i)
    print(index)
    if index == 12:
        print("Oualid is the nick name")

























