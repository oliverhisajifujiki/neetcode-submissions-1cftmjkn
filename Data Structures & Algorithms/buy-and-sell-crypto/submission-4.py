class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #like two pointer
        #but l = 0 and r = l + 1
        l, r = 0, 1
        best = 0 
        while l < r and r < len(prices):
            diff = prices[r] - prices[l]
            if diff < 0:
                l = r
                r += 1 
            else:
                if diff > best:
                    best = diff
                r += 1
        return best