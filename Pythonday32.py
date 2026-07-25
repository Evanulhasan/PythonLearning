# Set Methods in python 

# Union:
"""A fundamental operation that combines all 
unique elements from two or more sets into a 
single new set, without any repetition."""
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))
print(s1, s2)

print("\n")
# Intersection 
""" A new set containing only the elements 
that are common to all of the sets. """
print(s1.intersection(s2))
print("\n")

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Madrid"}

#UnionUpdaate
# cities.update(cities2)
# print(cities,"\n")

# intrsection_update
# cities3 = cities.intersection_update(cities2)
# print(cities)

# Symmetric_difference 
# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# difference : it show cities have and cities2 not 
# cities3 = cities.difference(cities2)
# print(cities3)

# #Isdisjoint set : they have on element is common
# cities3 = cities.isdisjoint(cities2)
# print(cities3)

# # is Supper set
# cities3 = cities.issuperset(cities2)
# print(cities3)

# Issubet()
cities3 = cities2.issubset(cities)
print(cities3)


# add()
cities.add("Bangladesh")
print(cities)

# Remove()/discard()
cities.remove("Tokyo")
print(cities)
# If item in not exist in set than raise error

# discard()
cities.discard("Tokyo1")
print(cities)
# If item not exist in set than not raise error

# pop()
item = cities.pop()
print(item)

# # del : delete intire set 
# del cities
# print(cities)

# Clear(): clear all item in the set and print empty set
cities.clear()
print(cities)


































