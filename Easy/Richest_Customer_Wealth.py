#
# 1672. Richest Customer Wealth https://leetcode.com/problems/richest-customer-wealth/
# 
# 
# Original Algorithm O(N^2) Time Comlpexity
#Runtime: 107 ms, faster than 32.41% of Python3 online submissions for Richest Customer Wealth.
#Memory Usage: 14 MB, less than 32.09% of Python3 online submissions for Richest Customer Wealth.
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
       
 
        richest = 0
        
        for account in range(len(accounts)):  # go through accounts
            current = 0
            for money in range(len(accounts[account])): # go through money in each account
                current += accounts[account][money]
            if current > richest:
                richest = current
        
        return richest
        