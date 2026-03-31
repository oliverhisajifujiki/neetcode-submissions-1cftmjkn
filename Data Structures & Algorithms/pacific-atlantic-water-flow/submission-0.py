#preliminary thoughts
    #the sort of naive way is checking for each cell if we can reach P and A 
    #the problem with this immediately is that we have to define where P and A 
        #access in the first place this though is not too hard? 
            #Pacific
            #so anything on heights[0][:] #first row
                #and anything on heights[:][0] #first coln
            
            #Atlantic
                #anyting on heights[-1][:] #last row
                #anything on heights[:][-1] #last coln
        
        #but the rule would look something like 
            #dfs each cell and check if it first can touch anything on the outer of the grid
            #we would mark a flag based of of what it touches 
            #so each cell would effectively have 2 flags , and visited or not ? another flag? 
            #a dictionary could be nice, where the value would be the cells index (i,j)
            #and the values would be three flags
            #we won't be doing that much overlap of path checking as if we have alr visited 
                #this particular cell it wouldn't be much of a problem we just check 
                    #if its in the dictionary we have visited and checked on it 
                    #so we might not even need a 3rd flag 

                    #THIS is the big problem, 
                        #the updates of these flags,
                        #if we can access each ocean
                        #would have to be updateed afterwards
                        #so we would need to store the cells we visit
                        #and only after the DFS ends we can update all their values 

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #a more elegant solution is:
        # take all cells that pacific can touch   
            #put in set # pac = set()
        #take all cells that atlantic can touch
            #put in set # atl = set()

        #because we are going from the ocean to land,
            #the movement logic is slightly flipped
            #instead of water flowing from high to low
            #ours goes from low to high 
        
        #take the intersection between all 

        rows = len(heights)
        cols = len(heights[0])

        #these will store all cells that reach each ocean
        pac = set()
        atl = set() 
        
        #store outside of function all the directions we can move from a given cell
        #up, down, right, left is how it will be defined
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        #define DFS after initialized cars
        def dfs(r,c,visited):
            #if we are in visited dont need to do anything just return
            if (r,c) in visited:
                return

            #if we are here we are visiting new cell
            visited.add((r,c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                #nr and nc are neighbour coords that we could potentiall take
                #skip them if they are out of bounds
                if nr < 0 or nc < 0 or nc >= cols or nr >= rows:
                    continue

                #now reverse flow logic
                if heights[nr][nc] < heights[r][c]:
                    continue #dont allow flow 
                
                #if we are here flow is allowed
                dfs(nr,nc,visited)
            

        #pacific DFS

        #top row
        for c in range(cols):
            dfs(0,c,pac)
        
        #left coln (excluding (0,0), visited in top row)
        for r in range(1, rows):
            dfs(r,0,pac)
        

        #atlantic DFS

        #bottom row
        for c in range(cols):
            dfs(rows -1, c, atl)
        
        #right coln (excluding (n,m))
        for r in range(rows-1):
            dfs(r,cols -1, atl)

        #get the intersection and return it, has to be a list of lists
        return [[r,c] for (r,c) in pac & atl] 








