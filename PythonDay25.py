# Tuples mathods in python 


# conntries = ("Spain", "Italy", "India", "China", "England", "Germany") 

# temp = list(conntries)
# temp.append("Russia")           # add item
# temp.pop(3)                    # Remove item
# temp[2]= "Finland"              # Change item 

# counntries = tuple(temp)
# print(counntries)


countries = ("Pakista", "Afghanistacn", "Bangladesh", "Shrilanka")
countries2 = ("Vietnam", "India", "China")

southEastAsia = countries + countries2
print(southEastAsia)


tup1 = (0, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9, 34, 45, 35, 12, 67, 3, 6, 3)
res = tup1.count(3)
print(res)
print("\n")
print(tup1.index(12,3,19))  # 12 in 14 index start 3, end 19
print(len(tup1))







































