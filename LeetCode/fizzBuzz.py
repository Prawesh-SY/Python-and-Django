from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result=[""]*n
        for i in range(0,n):
            if ((i+1)%3==0 and (i+1)%5==0):
                result[i]="FizzBuzz"
            elif (i+1)%3==0:
                result[i]='Fizz'
            elif (i+1)%5==0:
                result[i]='Buzz'
            else:
                result[i]=str(i+1)
        return result
    
    def fizzBuzzStringConcantation(self, n: int) -> List[str]:
        result=[""]*n
        for i in range(0,n):
            currentStr=""
            if (i+1)%3==0:
                currentStr+="Fizz"
            if (i+1)%5==0:
                currentStr+='Buzz'
            if currentStr=="":
                currentStr+=str(i+1)
            result[i]=currentStr
        return result

solution=Solution()
print(solution.fizzBuzz(n=21))
print(solution.fizzBuzzStringConcantation(n=21))

