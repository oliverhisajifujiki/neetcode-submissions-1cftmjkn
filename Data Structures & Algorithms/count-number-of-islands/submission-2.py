class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) 
        islandCounter = 0

        def dfs(r,c):
            #base case is we are out of bounds / reached water / revisting
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            
            grid[r][c] = "0" #we can do a specific visited value , but this works fine for the task

            #recursion, on all 4 directions
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islandCounter += 1
        
        return islandCounter





