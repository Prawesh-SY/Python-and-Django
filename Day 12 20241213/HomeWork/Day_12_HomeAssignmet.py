
displayMessage='''    
             Please select an option below:
1. Write a program to remove duplicate items from the list data = [2, 5, 5, 6, 2]
2. How would you find the maximum value in the dictionary {"a": 10, "b": 20, "c": 15}?
3. Convert the list [1, 2, 3, 4, 5] into a dictionary where the keys are the numbers and the values are their cubes.
4. Write a program to skip all numbers divisible by 3 while looping from 1 to 10.
5. Write a program to find whether 29 is a prime number or not.
6. Write a program to find the sum of all even numbers between 1 and 50. What will the output be?
'''
def removeDuplicate():
    data=[2,5,5,6,2]
    result =list(set(data))
    return result
def maximumValueInDict():
    myDict=dict(a=10,b=20,c=15)
    # print(myDict)
    max=0
    result={}
    for i in myDict.values():
        # print(i)
        if  int(i)>int(max):
            max=i
    for key,value in myDict.items():
        if max==value:
            result.update({key:value})
    return result,max
def dictComprehension():
    myList=[1, 2, 3, 4, 5]
    myDict={x:x**3 for x in  myList}
    return myDict
def skipDivisbles(num,skip):    #COMPLETED
    i=0
    while i<num:
        i+=1
        if i%skip==0:
            continue
        print(i)
    return True
def isPrime(num):
    for i in range(2,(int((num**0.5))+1)):
        if num%i==0:
            return False
    return True
def sumEven(start,stop):
    sum=0
    for i in range(start,stop+1):
        if i%2==0:
            sum=sum+i 
    return sum       
    

# result_1=removeDuplicate()
result_2=maximumValueInDict()
result_3=dictComprehension()
result_4=skipDivisbles(10,3)
result_5=isPrime(29)
result_6=sumEven(1,50)
# print(result_1)
# print(result_2)
# print(result_3)
print(result_4)
print(result_5)
print(result_6)