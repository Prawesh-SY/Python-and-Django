"""
What are logical operator in Python? Explain their types with example.
Logical operators in Python are used to combine conditional statements. They evaluate expressions to return boolean values (True or False). There are three primary logical operators in Python:

1. and
The and operator returns True if both expressions are True. If either of the expressions is False, it returns False.

Example:
"""
x = True
y = False
result = x and y
print(f"If x = {x} and y = {y}, then,\n x and y = ",result)  # Output: False

x = 5
print(f"If x = 5,\nthen\n x > 2 and x < 10 = {x > 2 and x < 10}")  # Output: True

"""
2. or
The or operator returns True if at least one of the expressions is True. It returns False only if both expressions are False.
Example:
"""
x = True
y = False
result = x or y
print(f"If x = True and y = False,\nthen\nx or y = {result}")  # Output: True

x = 5
print(f"If x = 5,\nthen\nx > 2 or x > 10= {x > 2 or x > 10}")  # Output: True

"""
3. not
The not operator returns True if the expression is False and vice versa. It is used to invert the boolean value.

Example:
"""
x = True
result = not x
print(f"If x =True,\nthen\nnot x={result}")  # Output: False

x = 5
print(f"If x = 5,\nthen\nnot (x > 2)={not (x > 2)}")  # Output: False

"""Summary
and: Both conditions must be True for the result to be True.

or: At least one condition must be True for the result to be True.

not: Inverts the boolean value of the expression."""

# How can we use xor, nor, nand logic?