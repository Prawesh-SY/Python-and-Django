#WAP to calculate the factorial of a given number using recursive function
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

#WAP to calculate the nth term of the Fabonacci's Series using recursive function
def fabonacci(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fabonacci(n-1) + fabonacci(n-2)
    pass

# Exercise 1: Tail Recursive Sum of Numbers
# Write a tail-recursive function to calculate the sum of the first n natural numbers.
def tailRecursiveSum(n, accumulator=0):
    if n==0:
        return accumulator
    else:
        return tailRecursiveSum(n-1,accumulator+n)
    pass
"""
Exercise 2: Non-Tail Recursive Sum of Numbers
Write a non-tail-recursive function to calculate the sum of the first n natural numbers.

Task:
Implement a non-tail-recursive function non_tail_recursive_sum(n) that returns the sum of numbers from 1 to n.
"""
def nonTailRecursiveSum(n):
    if n == 0:
        return 0
    else:
        return n+nonTailRecursiveSum(n-1)