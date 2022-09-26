# 1480. Running Sum of 1D Array https://leetcode.com/problems/running-sum-of-1d-array/
# 
# 
# Runtime: 86 ms, faster than 19.51% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14 MB, less than 72.70% of Python3 online submissions for Running Sum of 1d Array.
# 
# O(N-1) solution
#
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #faster solution starts at 1
        for num in range(1,len(nums)):
            nums[num] += nums[num-1]
            
        return nums
        
        # slower starts at 0
        '''
        size = len(nums)
        total = 0
        for num in range(size):
            total += nums[num]
            nums[num] = total
        return nums
        '''