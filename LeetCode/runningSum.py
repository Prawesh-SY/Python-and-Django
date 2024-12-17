from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                result[i]=nums[i]
            else:
                result[i]=result[i-1]+nums[i]
        return result

solution = Solution()
nums = [1,2,3,4,5,6,88]
print(solution.runningSum(nums))