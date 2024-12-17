# WAP to square the numbers in a given list

num=[1,2,3,4,5,5,4]
squNum=num.copy()
j=0
for i in num:
    num[j]= (i*i)
    j+=1
print(num)
print(squNum)