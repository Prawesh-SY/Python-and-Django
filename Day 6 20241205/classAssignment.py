"""count=1
while (count<=100):
    print(count)
    count=count+1
"""
"""
Write a pseudo code to print even number from 0  to 100

step1:    count = 1
step2:    top:
step3:        if (count <= 100)
step4:            if (count % 2 == 0)
step5:                print(f."{count} is even")
step6:        count = count +1
step7:        goto top

"""
"""
Loops and its types in Python
There are two types:
    1. while
    2. for

"""
"""
# WAP to print a number is even or odd from 1 to 50
count=1
while (count<=50):
    if (count%2==0):
        print(f"{count} is even")
    else:
        print(f"{count} is odd")
    count=count+1
"""
#WAP to find prime number upto 50 (python code)
import time
time1=time.time()
count = 1


while (count <= 5000):
    divisor=1
    x=0
    while (divisor <= count):
        mod=count%divisor
        if mod==0:           
            x=x+1
        if x>=3:    #to improve the time complexity we use this condition
            break
        divisor = divisor + 1
    if x<3:
        print(f'{count} is a prime')
    count =count+1
time2=time.time()
print(time2-time1)