#String in Python 
"""In Python, a String(str) is an immutable 
sequence of unicode characters used to store a 
manipulate text."""

name = "Evanul Hasan Oualid"
friend = 'Rohan'

print("Hello, " + name)

# We can single quotation('') or double quotation("")
apple = 'He said, "I want to eat an apple."'
print(apple)

# Multiline Strings we can use it 
# single quot or double quot but it will triple("""""")('''''')
selfintro = """Hi I'm Evanul Hasan Oualid,nice to meet you.
I am from Bangladesh.
I work as a data analyst."""
print(selfintro)

print(name[0])
print(len(name))
print(name[-19])


# for loop in string 
print("___________for loop start___________")
for i in name:
    print(i)
print("____________for loop End____________")
    
print(friend[0]) 
print(friend[1]) 
print(friend[2]) 
print(friend[3]) 
print(friend[4]) 
# print(friend[5]) # It's Throws an error Because of nothing in index-5 





















