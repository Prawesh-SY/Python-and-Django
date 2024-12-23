# WAP to print whole number using recursion fucntion (0 to 9)
def recursion(start,stop):
    if start==stop:
        return stop
    print(start)
    return recursion(start+1,stop)
def squareRecursion(start,stop):
    if start==stop:
        return stop**2
    print(start**2)
    return squareRecursion(start+1,stop)

# def fibonacciRecursion(n):
#     if n==1:
#         print (1)
#     elif n==0:
#         print(0)
#     else:
#         print()
#         return fibonacciRecursion(n-2)+fibonacciRecursion(n-1)


# # display=recursion(0,9)
# # print(display)


# # squarDisplay=squareRecursion(1,50)
# # print(squarDisplay)
# fib=fibonacciRecursion(9)

a=0
b=1
print(a,"\n",b)
for i in range(1000000):
    c = a + b
    print(c)
    a=b
    b=c

for i in range(50):
    pass