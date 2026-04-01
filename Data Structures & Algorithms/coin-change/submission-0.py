class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[a] = min # of coins needed to make amount a
        #
        # if we can not make a with the coins we will put inf
        dp = [float("inf")] * (amount + 1) 

        # base case:
        # takes 0 coins to make 0
        dp[0] = 0

        # now we populate dp, and we do this via adding each coin to the previous amortized amounts we got
        for a in range(1, amount + 1):
            #to get amount a, try each coin as a possible last coin
            for c in coins:
                #if coin c is too large, skip it
                
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c]) #this 1 + dp[a-c] is where we build up our array
                
        if dp[amount] == float("inf"):
            return -1
        
        return dp[amount] 
