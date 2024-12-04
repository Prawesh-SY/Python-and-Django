# Bitwise Operators in Python
# Bitwise operators are used to perform bit-level operations on integers. They operate on binary representations of numbers. Here are the common bitwise operators in Python:

# & (AND): Sets each bit to 1 if both bits are 1.

# | (OR): Sets each bit to 1 if one of two bits is 1.

# ^ (XOR): Sets each bit to 1 if only one of the two bits is 1.

# ~ (NOT): Inverts all the bits.

# << (Zero fill left shift): Shifts left by pushing zeros in from the right and letting the leftmost bits fall off.

# >> (Signed right shift): Shifts right by pushing copies of the leftmost bit in from the left and letting the rightmost bits fall off.

# Example:
a = 10  # In binary: 1010
b = 4   # In binary: 0100

# Bitwise AND
result_and = a & b
print(result_and)  # Output: 0 (0000 in binary)

# Bitwise OR
result_or = a | b
print(result_or)  # Output: 14 (1110 in binary)

# Bitwise XOR
result_xor = a ^ b
print(result_xor)  # Output: 14 (1110 in binary)

# Bitwise NOT
result_not = ~a
print(result_not)  # Output: -11 (In binary: ...11110101)

# Bitwise Left Shift
result_left_shift = a << 2
print(result_left_shift)  # Output: 40 (101000 in binary)

# Bitwise Right Shift
result_right_shift = a >> 2
print(result_right_shift)  # Output: 2 (10 in binary)


# != Operator in Python
# The != operator is a comparison operator that checks if two values are not equal. It returns True if the values are not equal and False if they are equal.

# Example:
x = 5
y = 10

result = x != y
print(result)  # Output: True

x = 5
y = 5

result = x != y
print(result)  # Output: False

# Summary
# Bitwise Operators: Perform bit-level operations on integers, such as AND, OR, XOR, NOT, left shift, and right shift.

# != Operator: Compares two values and returns True if they are not equal and False if they are equal.