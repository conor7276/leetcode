# 1342 Number of Steps to Reduce a Number to Zero https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
# Runtime 54ms Beats 46.19% 
# Memory 13.7 MB Beats 95.35%
# O(1) solution time and space
class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
                res += 1
            else:
                num -= 1
                res += 1
        return res
