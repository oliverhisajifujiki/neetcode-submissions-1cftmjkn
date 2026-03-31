class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #go along grid, when we see land, we will do a dfs on all adjacent grids 
        #we mark every land that connects these islands then we +1 to our island count
        #we then geet moving along the grid until we see land we have not visited yet 



        rows = len(grid)
        cols = len(grid[0])
        islandCounter = 0

        def dfs(r,c): #takes in the current location and marks everything into a grid
            #make sure r,c is not in water or out of bounds
            if r >= rows or r < 0 or c < 0 or c >= cols or grid[r][c] == "0":
                return

            #we could mark the visited land something cool like "X" 
            #but to fit nicely into our logic lets just mark it "0"
            #this way we don't have to change anythign and we alr skip it 
            grid[r][c] = "0"  

            #explore all four directoins 
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1) 
            dfs(r, c - 1)
            
        r = 0 
       
        while r < rows:
            c = 0
            while c < cols:
                if grid[r][c] == "0": #this is water we move along
                    c += 1
                else: #we are seeing land! 
                    dfs(r,c) #use DFS to mark all the island so we dont double count
                    islandCounter += 1
                    c += 1
                
            r += 1
        
        return islandCounter


        