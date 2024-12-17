# 1342. Number of Steps to Reduce a Number to Zero

class Solution:
    def numberOfSteps(self, num: int)-> int:
        counter = 0
        result=num
        while result>0:            
            if result%2==0:
               result /= 2    # result=result/2  
            else:
                result -= 1        # result=result-1 
            counter+= 1          # counter=counter+1
        return counter
    def numberOfStepsBitwiseOpertion(self, num: int)-> int:
        counter = 0
        result = int(num)
        while result > 0:            
            if result & 1 == 0:
                result >>= 1    # Right shift to divide by two
            else:
                result -= 1
            counter += 1
            print(result)

        return counter


solution=Solution()
command ='y'
while command=='y':
    count=solution.numberOfStepsBitwiseOpertion(num=int(input('Enter a number: ')))
    print(f'It take {count} steps to reduce your number to zero')
    command=input("Do you wish to check next number (y/n): ")