# File IO read(), readline(), readlines() methods in Python 

# with open("sample.txt", "w") as file:
#     file.write("Hello, this is a sample text file.\n and it contains multiple lines of text.\n This is the third line.\n")

# with open("sample.txt", "r") as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line.strip())



# readline() method reads one line at a time from the file, and it returns an empty string when it reaches the end of the file. The strip() method is used to remove any leading or trailing whitespace characters (including the newline character) from the line before printing it.
# with open("marks.txt","w", encoding="utf-8") as file:
#     file.write("85,66,45\n")
#     file.write("92,88,95\n")
#     file.write("78,82,80\n")
    
    
# i = 0 
# with open("marks.txt","r", encoding="utf-8") as file:
#     while True:
#         i = i + 1 
#         line = file.readline()
#         if not line:
#             break
#         m1, m2, m3 = map(int, line.strip().split(","))
#         print(f"Marks of Student {i} in Math is: {m1}")
#         print(f"Marks of Student {i} in Science is: {m2}")
#         print(f"Marks of Student {i} in English is: {m3}")

#         print(line,"\n")


# writelines() method is used to write multiple lines to a file at once. It takes a list of strings as input, where each string represents a line to be written to the file. The method writes each string in the list to the file, adding a newline character after each string.

with open("sample.txt", "w", encoding="utf-8") as file:
    lines = ["Hello, this is a sample text file.\n", "It contains multiple lines of text.\n", "This is the third line.\n"]
    file.writelines(lines)









