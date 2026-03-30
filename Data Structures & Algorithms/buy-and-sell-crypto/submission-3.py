class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #like two pointer here technically 
        #start with l = 0 and r = 1 and best = 0. now while l < r 
        #if prices[l] > prices[r] ever is the case l = r 
        #else move r += 1 (also if the price beats best save it)
        l = 0
        r = 1
        best = 0
        while l < r and r < len(prices):
            diff = prices[r] - prices[l]
            if diff < 0: #prices[r] < prices[l]
                l = r
                r += 1
            else:
                if diff > best:
                    best = diff
                r += 1
        return best