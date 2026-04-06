class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        best = 0
        while r < len(prices):
            gain = prices[r] - prices[l]

            if gain > best:
                best = gain
            
            elif gain < 0:
                l = r
            r += 1
        
        return best
