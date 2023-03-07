#121 Best Time to Buy and Sell Stock

# O(N) Dynamic Programming Solution
# Runtime 93.1% Memory 96.65%

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum = prices[0] # keep track of minimum price
        min_index = 0 # keep track of the index of the minimum price
        maximum = 0 # keep track of maximum price
        max_index = 0 # keep track of the index of the maximum price
        max_profit = 0 # keep track of the max profit
        

        for price in range(1, len(prices)):
            if prices[price] <= minimum: # check for minimum
                minimum = prices[price]
                min_index = price
                if(min_index > max_index):
                    # if minimum index is greater than the max it means that the max
                    # is no longer valid and a new one must be found
                    maximum = 0
                    max_index = min_index
            elif prices[price] >= maximum: # check for maximum
                maximum = prices[price]
                max_index = price
            if(maximum - minimum > max_profit and min_index < max_index): 
                # check if current profit is bigger than the max.
                # also check if the indexes are valid for it to be a max.
                # the minimum index cannot come after the maximum index.
                max_profit = maximum - minimum

        print(minimum, maximum)
        return max_profit
