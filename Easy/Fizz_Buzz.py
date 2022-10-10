# 412. FizzBuzz https://leetcode.com/problems/fizz-buzz/description/
# Runtime 98ms Beats 10.70%
# Memory 15Mb Beats 43.55% 
# O(N) time
# O(1) space
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for num in range(1,n+1):
            if num % 3 == 0 and num % 5 == 0:
                res.append("FizzBuzz")
            else:
                if num % 3 == 0:
                    res.append("Fizz")
                elif num % 5 == 0:
                    res.append("Buzz")
                else:
                    res.append(str(num))
        return res
