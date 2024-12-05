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