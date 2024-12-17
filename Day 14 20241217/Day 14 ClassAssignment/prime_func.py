def isPrime(num):
    count=0
    for i in range(1,num):
        if num % i ==  0:
            count+=1
            if count>3:
                return False
                break
    return True
def isPrimeSirMethod(num):
    for i in range(2,num):
        print(i)
        if num%i==0:
            return False
    return True
def isEven(num):
    if num%2==0:
        return True
def isDivisibleBy3(num):
    if num%3==0:
        return True
        
num=int(input("Enter the number you wish to check: "))
resultisPrime=isPrime(num)
resultisPrimeSirMethod=isPrimeSirMethod(num)
resultisEven=isEven(num)
resultIsDivisibleBy3=isDivisibleBy3(num)
if resultisPrimeSirMethod==True:
    print(f"The number {num} is a prime number")
else:
    print(f"The number {num} is a composite number")
if resultisEven==True:
    print(f"The number {num} is an even number")
else:
    print(f"The number {num} is a odd number")
