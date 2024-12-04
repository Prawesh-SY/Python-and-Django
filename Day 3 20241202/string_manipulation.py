"""
Concantation
strip() 
    -Used to remove space before and after the last string in a group of string.
    -Does not require an argument

split()
    -Need an argument
    -splits the string based on the character passed as an argument

replace()
    -needs two arguments
    -replaces the first argument with the second argument

upper()
    -needs no argument
    -capitalizes all the characters

capitalize()
    -needs no argument
    -capitalizes the first character of the strings    

title()
    -needs no argument
    -capitalizes the first character of every string


"""
# print("           Hello, this is Prawesh                      ".strip())
# print("      Hello, this is Prawesh                      ")

# String manipulation is a fundamental aspect of Python programming. Here are ten commonly used string manipulation functions in Python:

### 1. **`len()`**
# Returns the length of the string.
#### Example:
string = "Hello, World!"
print(len(string))  # Output: 13

### 2. **`str()`**
# Converts an object to a string.
#### Example:
number = 123
print(str(number))  # Output: "123"

### 3. **`lower()`**
# Converts all characters in the string to lowercase.
#### Example:
string = "HELLO"
print(string.lower())  # Output: "hello"


# 4. lstrip() and rstrip()
# lstrip(): Removes leading whitespace from the string.
# rstrip(): Removes trailing whitespace from the string.
# Example:
string = "   Hello, World!   "
print(string.lstrip())  # Output: "Hello, World!   "
print(string.rstrip())  # Output: "   Hello, World!"

### 5.  translate()
# Replaces characters in a string using a translation table.
# Example:
string = "Hello, World!"
translation_table = str.maketrans("World","Earth")
print(string.translate(translation_table))  # Output: "Hello, Earth!"
# Note: The first two maketrans arguments must have equal lenth

### 6. partition()
# Splits the string into three parts: the part before the separator, the separator itself, and the part after the separator.
# Example:
string = "Hello, World!"
print(string.partition(","))  

### 7. **`split()`**
# Splits the string into a list of substrings based on a specified delimiter.
#### Example:
string = "Hello, World!"
print(string.split(","))  # Output: ['Hello', ' World!']

### 8. **`join()`**
# Joins elements of an iterable (like a list) into a single string, with a specified separator.
#### Example:
list_of_strings = ["Hello", "World"]
print(" ".join(list_of_strings))  # Output: "Hello World"

### 9. **`find()`**
# Returns the lowest index of the substring if found in the string. Returns -1 if the substring is not found.
#### Example:
string = "Hello, World!"
print(string.find("World"))  # Output: 7

### 10. **`format()`**
# Formats specified values in a string.
#### Example:
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  # Output: "My name is John and I am 30 years old."


