# os Module in Python 
# os module in Python provides a way of using operating
# system dependent functionality like reading or writing
# to the file system, interacting with the environment,
# and managing processes. It allows you to perform tasks
# such as creating directories, listing files, and 
# executing shell commands.


import os 

# This is a simple script to create folders and 
# list them using the os module in Python.
# if (not os.path.exists("data")):
#     os.mkdir("data")

# Here we are creating 100 folders named Day1, 
# Day2, ..., Day100
# for i in range(1,101):
#     os.mkdir(f"data/Day{i}")

# Here we are deleting all the folders in the "data" 
# directory
# for i in range(1,101):
#     os.rmdir(f"data/Day{i}")

# Here we are renaming all the folders in the "data"
# for i in range(1,101):
#     os.rename(f"data/Day{i}", f"data/PythonDay{i}")

 # This function returns the current 
 # working directory of a process.
print(os.getcwd())


























