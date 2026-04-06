class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        best = 0
        while l < r and r < len(prices):
            diff = prices[r] - prices[l]
            if diff < 0: #prices[l] > prices[r]
                l = r
                r += 1
            elif diff > best:
                best = diff
            else:
                r += 1
        return best