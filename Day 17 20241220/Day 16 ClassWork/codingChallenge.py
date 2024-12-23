# WAPP that asks the user to input a number and then prints whether the number is even or odd.
def isEven():
    num=int(input("Enter a number: "))

    if num%2==0:
        print(f"The number {num} is even")

    else:
        print(f'The number {num} is odd')
# Write a program that finds the highest and lowest digit in a given string of numbers.
# Example Input: "6787654445678"
# Example Output: Highest = 8, Lowest = 4
def maxMin(num):
    for j in num:
        max=j
        min=j
    for i in num:
        if int(max)>int(i):
            max=i
            pass
        if int(min)<int(i):
            min=i

    print(f"The largest number in the list is {max}")
    print(f"The smallest number in the list is {min}")
    pass

# Write a program that takes a sentence as input and counts the number of words in it.
def wordCounter(string):
    words=string.split(" ")
    print(len(words))
    pass
# Write a Python program that takes a positive interger as input and calculates the sum of its digits.
def digitadder(num):
    if num<0:
        print("Please input positive number")
    else:
        numString=str(num)
        add=0
        for i in numString:
            add=add+int(i)
        print("Sum of the digits = ",add)
        pass
    pass
# Write a program that takes a string as input and prints the string in reverse order.
def stringReverser(string):
    pass

# Write a program that checks if a given word is a palidrome (reads the same forwards and backwards).
def isPanidrom(string):
    pass

# WAP that calculates the factorial of a given number n (where n is provided by the user).
def factorial(num):
    pass

# WAP that counts the number of vowels in a given string.
def countVowels(string):
    pass

# WAP that takes a number n as input and prints the square of all numbers from 1 to n.
def squarer(num):
    pass

# Write a Python porgram(WAPP) that takes a number as input and checks whether it is positive, negative, or zero.
def numberLine(num):
    pass

# WAP that prints the following pattern:
# *
# **
# ***
# ****
# *****
def prymid(num):
    pass

# WAP function that takes a string as input and returns a dictionary where the keys are the words in the string, and valuse are the lengths of those words.
def lenthCal(string):
    pass

# WAPP that takes a list of students' names and their corresponding marks in a subject, stores them in a dictionary, and then calculates and prints the average mark.
# Example Input: ["Alice","Bob","Charles"] and [85, 92,78]
# Example Output: {'Alice':'85', 'Bob':'92', 'Charles':'78'} and Average = 85
def studentAverage():
    pass




# isEven()
# maxMin("987363")
wordCounter("Manoj Sir is legendary")
digitadder(-55)
