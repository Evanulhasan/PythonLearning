# String Methods 

# String are immutable sequence of characters. In python.

a = "Evanul Hasan Oualid"
print(len(a))

print(a.upper())
print(a.lower())

str1 = "!!! Eva!!nul !!!!"
print(str1.rstrip("!"))  # Remove the trailing characters
print(str1.lstrip("!"))  # Remove the leading characters
print(str1.strip("!"))  # Remove the leading and trailing characters

print(a.replace("Evanul", "John"))  # Replace a substring with another substring
print(a.split(" "))  # Split the string into a list of substrings based on a delimiter

Heading = "introduction to python"
print(Heading.capitalize())  # Capitalize the first letter of the string
print(Heading.title())  # Capitalize the first letter of each word in the string
print(a.center(50, "#"))  # Center the string within a specified width and fill with a specified character
print(a.count("a"))  # Count the occurrences of a substring in the string
print(a.endswith("Oualid"))  # Check if the string ends with a specified substring
print(a.startswith("Evanul"))  # Check if the string starts with a specified substring

str2 = "Welcome to the Console Application"
print(str2.endswith("to", 4, 10))  # Check if the substring from index 4 to 10 ends with "to"
print(str2.startswith("Welcome", 0, 7))  # Check if the substring from index 0 to 7 starts with "Welcome"
str3= "He's name is Dan.He is an honest man."
print(str3.find("is"))  # Find the index of the first occurrence of a substring in the string
print(str3.index("is"))  # Find the index of the first occurrence of a substring in the string (raises ValueError if not found)
str4 = "EvanulHasanOualidIamformBangladesh"
print(str4.isalnum())  # Check if all characters in the string are alphanumeric
print(str4.isalpha())  # Check if all characters in the string are alphabetic
print(str4.islower())  # Check if all characters in the string are lowercase
print(str4.isprintable())  # Check if all characters in the string are printable
str5 = "    "
print(str5.isspace())  # Check if all characters in the string are whitespace
str6 = "larning python is fun"
print(str6.istitle())  # Check if the string is in title case
str7 = "Python Is A Programming Language"
print(str7.istitle())  # Check if the string is in title case

print(str7.swapcase())  # Swap the case of all characters in the string








