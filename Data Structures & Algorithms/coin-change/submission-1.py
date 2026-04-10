class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [ float("inf") ] * (amount + 1) #initialize this array
                                    #as we are going to be finding the min
                                    #we will check if something is smaller 
                                    #so we init to "inf"
        dp[0] = 0 #0 coins to make up 0 dollars

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        
        if dp[amount] == float("inf"):
             #never could make it 
             return -1
        return dp[amount]

        