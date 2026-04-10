class Solution:
    def climbStairs(self, n: int) -> int:
        #base case n <= 2, theres only 1 way to climb 1 step
        #therea are 2 ways to climb up 2 steps (1 + 1 or 2)

        if n <= 2:
            return n
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n-1]
            