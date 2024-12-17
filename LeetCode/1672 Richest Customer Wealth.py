from typing import List
class Solution:
    def maximumWealth(self, accounts:List[List[int]])->int:
        CustomerWealth= [0]*len(accounts)
        richestCustomer=0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                CustomerWealth[i] += accounts[i][j]
            if richestCustomer<CustomerWealth[i]:
                richestCustomer=CustomerWealth[i]
        return richestCustomer

solution=Solution()
accounts=[[1,2,3],[3,4,5],[1,2,3,4,5,6]]
print(solution.maximumWealth(accounts))