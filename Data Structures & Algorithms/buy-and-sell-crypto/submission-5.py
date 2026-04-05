class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 #buy
        r = 1 #sell
        b = 0
        while l < r and r < len(prices):
            diff = prices[r] - prices[l]
            if diff < 0: #prices[l] > prices[r]
                #as we are iterating through the list 1 by 1, we know this switch always wat we want
                l = r
                r += 1
            else: #we at least don't lose money
                #check if diff is better than best 
                if diff > b:
                    b = diff
                
                r += 1
        return b
