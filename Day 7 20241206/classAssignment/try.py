'''
command='y'
while command=='y':
     num=int(input("Enter the number: "))
     if(num<0):
          print("The number is negative")
     elif(num==0):
          print("The number is zero")
     else:
          print("The number is positive")

     command=input("Do you wish to continue (y/n): ")
'''

n=5
if n & 1==0: #bit-wise operation to check the last bit
     print('Even')
else:
     print('Odd')

"""
Explanation:
All the even number when converted to bit will have last bit as '0'. And all the odd number when converted to bit will have last bit as '1'. Hence,
for even: 0 & 1 = 0
for odd: 1 & 1 = 1
"""