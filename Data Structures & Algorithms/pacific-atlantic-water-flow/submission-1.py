class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pcf = set()
        atl = set()

        def dfs(r,c,visited):
            if (r,c) in visited:
                return #base case
            
            visited.add((r,c))

            #now we see if any of hte four directions we go along will work 
            for (dr, dc) in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue 
                
                #now if the flow isn't allowed we also skip nc / nr
                #because we are going in reverse we check if it is smaller than where we came
                #if it is smaller we aren't allowed
                if heights[nr][nc] < heights[r][c]:
                    continue
                
                #if all of thse are okay we continue the dfs
                dfs(nr,nc,visited)
            
        #now we go through all of the cells touching the pcf
        for r in range(rows):
            dfs(r,0,pcf)

        for c in range(cols):
            dfs(0,c,pcf)
        
        for r in range(rows):
            dfs(r, cols - 1, atl)
        
        for c in range(cols):
            dfs(rows - 1, c, atl)

        return [[r,c] for (r,c) in pcf & atl]



