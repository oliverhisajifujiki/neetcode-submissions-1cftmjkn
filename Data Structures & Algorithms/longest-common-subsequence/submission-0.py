class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp= [[0] * (n+1) for _ in range (m+1)]

        #dp[i][j] = longest common subseuence of text1[:i] and text2[:j]

        #start at 1 because dp[0][*] and dp[*][0] are 0 for any *
        #if a string prefix is empty, common subsequence is length 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                #the current new chars are text1[i-1] and text2[j-1]
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    #they dont match 
                    #skip the new char from text1 
                    #or skip the new char from text2
                    #take the max of either result
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]