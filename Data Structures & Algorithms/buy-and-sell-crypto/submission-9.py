class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        best = 0
        while r < len(prices):
            gain = prices[r] - prices[l]
            if gain < 0: #as we are incrementing by 1 alays safe to set l = r
                l = r
            elif gain > best:
                best = gain
            r += 1
        return best 