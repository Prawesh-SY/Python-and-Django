
# What is data structure?
"""
Ans: Data structure is a specialized format for organizing, managing and storing data in the computer so that it can be used effeciently. Different types of data structure are suited to different kinds of applications, and some are highly specialized to specific tasks.
"""
# What are the types of data structure?
"""
Ans: Python offers a variety of built-in data structures that are essential for organizing and managing data effectively. Here are the primary types:

### **1. Lists**
- **Description**: Ordered, mutable collections of items.
- **Syntax**: Defined using square brackets `[]`.
- **Example**:
"""
my_list = [1, 2, 3, 4, 5]
"""
### **2. Tuples**
- **Description**: Ordered, immutable collections of items.
- **Syntax**: Defined using parentheses `()`.
- **Example**:
"""
my_tuple = (1, 2, 3, 4, 5)
"""
### **3. Sets**
- **Description**: Unordered collections of unique items.
- **Syntax**: Defined using curly braces `{}` or the `set()` function.
- **Example**:
"""
my_set = {1, 2, 3, 4, 5}

"""
### **4. Dictionaries**
- **Description**: Unordered collections of key-value pairs.
- **Syntax**: Defined using curly braces `{}` with key-value pairs separated by colons.
- **Example**:
"""
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

"""
### **5. Strings**
- **Description**: Ordered collections of characters (text).
- **Syntax**: Defined using single, double, or triple quotes.
- **Example**:
"""
my_string = "Hello, World!"

"""
### **6. Arrays**
- **Description**: Ordered collections of items, typically of the same type, more efficient for numerical operations. Provided by external libraries like `array` and `numpy`.
- **Syntax**: Defined using `array` module or `numpy` library.
- **Example with `array` module**:
  """
import array as arr
my_array = arr.array('i', [1, 2, 3, 4, 5])

# - **Example with `numpy` library**:
import numpy as np
my_numpy_array = np.array([1, 2, 3, 4, 5])

"""
### **7. Lists of Lists (2D Arrays)**
- **Description**: Lists that contain other lists as elements, used for representing 2D data.
- **Syntax**: Defined using nested square brackets.
- **Example**:
"""
my_2d_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""
### **8. Deques**
- **Description**: Double-ended queues that allow appending and popping from both ends, provided by the `collections` module.
- **Syntax**: Defined using the `deque` class from the `collections` module.
- **Example**:
"""
  # from collections import deque
my_deque = deque([1, 2, 3, 4, 5])

"""
These built-in data structures are fundamental tools in Python, each offering unique capabilities for different use cases. Whether you need an ordered collection, an immutable sequence, or a structure for numerical operations, Python has you covered.
"""

# What is list? Explain with the help of examples. How to create a list? How to access list items using while and for loop? How to add and remove item from a list? How to change value of list?
"""
### What is a List?
A list in Python is an ordered and mutable collection of items. Lists can store elements of different types, including numbers, strings, and even other lists. They are one of the most versatile and commonly used data structures in Python.

### How to Create a List?
Lists are created by placing the elements inside square brackets `[]`, separated by commas.
#### Example:
"""
# Creating a list of integers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]

# Creating a mixed list
mixed = [1, "apple", 3.14, True]
"""


### How to Accessing List Items Using a `while` Loop
You can use a `while` loop to access items in a list by their index.
#### Example:
"""
# Define a list
fruits = ["apple", "banana", "cherry"]

# Initialize index
i = 0

# Use a while loop to access list items
while i < len(fruits):
    print(fruits[i])
    i += 1

# Output:
# apple
# banana
# cherry
"""

### How to Accessing List Items Using a `for` Loop
You can use a `for` loop to iterate over the elements of a list directly.
#### Example:
"""
# Define a list
fruits = ["apple", "banana", "cherry"]

# Use a for loop to access list items
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
"""

### Explanation:
- **Creating Lists**: Lists are created using square brackets with elements separated by commas. They can contain different types of elements.
- **`while` Loop**:
  - Initialize the index to 0.
  - Use the `while` loop to iterate as long as the index is less than the length of the list.
  - Print the element at the current index and increment the index.
- **`for` Loop**:
  - Directly iterate over the elements of the list using a `for` loop.
  - Print each element during the iteration.
These methods demonstrate how to create and access list items in Python using both `while` and `for` loops.

Manipulating lists in Python is quite flexible and straightforward. You can add, remove, and change values using various methods. Here's how you can do it:
### How to Adding Items to a List
1. **`append()` Method**: Adds an item to the end of the list.
"""
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
"""
2. **`insert()` Method**: Adds an item at a specified position.
"""
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "blueberry")
print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry']
"""
3. **`extend()` Method**: Adds elements from another list to the end of the list.
"""
fruits = ["apple", "banana", "cherry"]
more_fruits = ["date", "elderberry"]
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']
"""

### How to Removing Items from a List
1. **`remove()` Method**: Removes the first occurrence of a specified item.
"""
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']
"""
2. **`pop()` Method**: Removes the item at a specified position (or the last item if no position is specified) and returns it.
"""
fruits = ["apple", "banana", "cherry"]
fruit = fruits.pop(1)
print(fruit)  # Output: banana
print(fruits)  # Output: ['apple', 'cherry']
"""
3. **`del` Statement**: Removes an item at a specified position or removes a slice of items.
"""
fruits = ["apple", "banana", "cherry"]
del fruits[1]
print(fruits)  # Output: ['apple', 'cherry']

# Removing a slice of items
fruits = ["apple", "banana", "cherry", "date"]
del fruits[1:3]
print(fruits)  # Output: ['apple', 'date']
"""
4. **`clear()` Method**: Removes all items from the list.
"""
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  # Output: []
"""
### How to Changing Values in a List
1. **Index Assignment**: Directly change the value of an item at a specific position.
"""
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']
"""
### Using Loops to Access and Modify List Items
#### Using a `while` Loop:
"""
fruits = ["apple", "banana", "cherry"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1
"""
#### Using a `for` Loop:
"""
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
"""
### Summary
- **Adding Items**: Use `append()`, `insert()`, and `extend()` methods.
- **Removing Items**: Use `remove()`, `pop()`, `del`, and `clear()` methods.
- **Changing Values**: Directly assign new values using indices.
- **Accessing Items**: Use loops like `while` and `for` to iterate over list items.

These methods provide a comprehensive toolkit for managing list data in Python.
"""

# data = [1,2,4] data[2] == 4

# What is dictionary with example? How to create dictionary? How can you access item from dictionary? How to add key and value to dictionary?
"""https://www.geeksforgeeks.org/python-dictionary/?ref=shm"""