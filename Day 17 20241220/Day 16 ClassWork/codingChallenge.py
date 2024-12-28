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

# Write a program that takes a string as input and prints the string in reverse order.
def stringReverser(string):
    reverseString=''
    # print(len(string))
    # print(string[len(string)-1])
    for z in range((len(string)-1),-1,-1):
        # print(z)
        reverseString = reverseString+string[z]        
    print(reverseString)


# Write a program that checks if a given word is a palidrome (reads the same forwards and backwards).
def isPalindrom(string):
    stringTest=string.replace(" ","").lower()
    if stringTest[::-1] == stringTest:
        print(f"'{string}' is a PALINDROME")
    else:
        print(f"'{string}' is NOT a PALINDROME")



# WAP that calculates the factorial of a given number n (where n is provided by the user).
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
    pass

# WAP that counts the number of vowels in a given string.
def countVowels(string):
    count=0
    for i in string:
        if i == 'a' or "A" or 'e' or 'E' or 'i' or 'I' or 'o' or 'O' or 'u' or 'U':#or i == 'e' or i=='i' or i=='o' or i=='u':
            count += 1
    print(f"There are {count} vowels in the string")
        

# WAP that takes a number n as input and prints the square of all numbers from 1 to n.
def squarer(num):
    if num==0:
        return 0
    else:
        return num**2+squarer(num-1)

def summer(n):
    if n==0:
        return 0
    else:
        return n + summer(n-1)

# Write a Python porgram(WAPP) that takes a number as input and checks whether it is positive, negative, or zero.
def numberChecker(num):
    if num<0:
        print(f"The number is negative")
    elif num>0:
        print(f"The number is positive")
    else:
        print(f"The number is zero")

# WAP that prints the following pattern:
# *
# **
# ***
# ****
# *****
def prymid(num):
    spacer=int(num/2)
    for i in range(1,num+1):
        space=" "*spacer
        for j in range(i):
            print(space,"*",end="")
        # print("\n")w
        spacer -= 1

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
# wordCounter("Manoj Sir is legendary")
# digitadder(-55)
# stringReverser(string="Python says Hello!!")
# isPalindrom(string="The way yaw eht")
# print(factorial(5))
# countVowels(string="Na cheka na muhaar sringaara le, Chandrama ma pani daag hunxa")
# print(squarer(num=10))
# print(summer(80))
# numberChecker(num=-30)
prymid(num=10)

