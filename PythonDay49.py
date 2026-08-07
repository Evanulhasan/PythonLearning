# File Io in Python 

# f = open("test.txt", "w")  # Open the file in write mode
# f.write("Hello, World!")  # This will write to the file
# f.close()  # Close the file

# f = open("test.txt", "r")  # Open the file in read mode
# content = f.read()  # Read the content of the file
# print(content)  # Print the content to the console
# f.close()  # Close the file

# f = open("test.txt", "a")  # Open the file in append mode
# f.write("\nThis is an appended line.")  # This will append to the file
# f.close()  # Close the file

# f = open("test.txt", "r")  # Open the file in read mode again
# content = f.read()  # Read the content of the file
# print(content)  # Print the content to the console
# f.close()  # Close the file


# Using 'with' statement for file handling
# Advantages of using 'with' statement:
# 1. It automatically takes care of closing the file after the block of code is executed
# 2. It makes the code cleaner and more readable
# 3. It helps to avoid potential file handling errors

with open("example.txt", "w") as f:
    f.write("This is an example of using 'with' statement for file handling.")

with open("example.txt", "r") as f:
    content = f.read()
    print(content)
    
with open("example.txt", "a") as f:
    f.write("\nThis line is appended using 'with' statement.")


with open("example.txt", "r") as f:
    content = f.read()
    print(content)





















