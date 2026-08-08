# Seek(), tell(), and truncate() are methods used in file handling in Python.

# with open('example.txt', 'r') as file:
#     print(type(file))  # This will print the type of the file object

#     # Move the cursor to the beginning of the file
#     file.seek(13)  
    
#     print(file.tell())  # This will print the current position of the cursor in the file
#     data = file.read(5)  # Read 5 characters from the current position
#     print(data)  # This will print the 5 characters read from the file
    

with open('sample.txt', 'w') as file:
    file.write("Hello, world! This is a sample text file.\n")
    file.truncate(20)  # Truncate the file to 20 bytes
    
with open('sample.txt', 'r') as file:
    print(file.read())  # This will print the remaining content of the file after truncation



















