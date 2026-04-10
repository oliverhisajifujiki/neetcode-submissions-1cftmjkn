class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #here we go along until we see a 1, once we see a 1, we do dfs 
        #and every piece of land that we see we mark with an x
        
        rows = len(grid)
        cols = len(grid[0])

        islandCounter = 0

        def dfs(r,c):
            #base case if we are out of bounds or if we see water or we have visited alr
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            #mark on our grid that we visited here
            grid[r][c] = "0" #if we wanted better tracking or a "nondestructive" approach
                                #we could mark it with like an X , but this flows well
                                #with logic
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1) #do recursion on all 4 directions

        #now we go along the whole grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islandCounter += 1
        
        return islandCounter


