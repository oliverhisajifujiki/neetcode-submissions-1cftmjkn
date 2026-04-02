class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #because you can only move down or right,
        #if the goal is to get to any of the cells on the first row or coln of any grid
        #there is only one way of getting to any of those cells
        #we can build the number of paths in this way

        #dp[r][c] = number of ways to reach cell (r,c)
        dp = [[1]*n for i in range(m)]

        #start from row 1 and col 1 and the row 0 and col 0 are alr filled in properly
        for r in range(1,m):
            for c in range(1,n):
                #here is the key logic, the number of ways to get from (r,c)
                #is equal to the number of ways it took to get from a cell to the left of it or to the right of it
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[m-1][n-1] 