#Dictionaries in Python 


dic = {
    "Evanul": "Human being", 
    "Spoon": "object"
}

print(dic["Evanul"])



info = {'name':"Karan", 'age':19, 'eligible': True}
print(info)
print(info['name'])
# print(info['name2']) # It show error 
print(info.get('name2')) # In not exist show none not error
print(info.keys())
print(info.values())

print("\n")
emid={
    344: "Evanul",
    56: "Tanvir",
    678: "Zakir",
    567: "Neha"
}
print(emid[56])

for key in emid.keys():
    print(emid[key])
    
print(emid.items())
    

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")





















