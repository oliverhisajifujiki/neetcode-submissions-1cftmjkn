class Solution:
    def climbStairs(self, n: int) -> int:
        #only 2 choices to make either take 1 step or 2
        #therefore to get all the ways to get up n stairs
            #either take 1 step from all the possible ways from n-1 stiars
            #or take 2 steps from all possible ways from n-2 stairs

        #base case 1 stair 
        #if n == 1:
        #    return 1
        #base case 2 stair
        #if n == 2:
        #    return 2
        #can combine these
        if n <= 2:
            return n

        dp = [0] * (n+1) #create an array of length n 
        #each element i will count the number of ways to get up i stairs
        dp[1] = 1
        dp[2] = 2 #base cases

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] #all ways with 1 step + all ways with 2 steps

        return dp[n]