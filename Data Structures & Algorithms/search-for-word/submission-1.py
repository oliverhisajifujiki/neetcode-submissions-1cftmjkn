class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #as we are trying many cells / finding valid configuartion
        #get 4 candidates, if one doesn't work back track
        #
        #we go through each board cell as a starting point
            #if board[r][c] matches word[i] continue
                #recurse in 4 directions
                    #mark cell as visited during this path
                #unmark when backtracking

        rows = len(board)
        cols = len(board[0])

        #r is the row index c is col index, i is how many matching chars we have so far
        def dfs(r,c,i): #returns true if we find the word else false
            if i==len(word): #we have all the matching chars 
                return True
            
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return False #our search is beyond the this current track is no good backtrack!
            if board[r][c] != word[i]:
                return False #doesn't match stop and backtrack

            #note if we reach here we have found a match for the correct char
            
            #we want a way of marking which letters we have alr visited
            #therefore we store the letters we have visited in temp and replace it with non letter
            temp = board[r][c]
            board[r][c] = "#"

            #try to see if any direction matches the next char
            nxt = i + 1
            found = (
                dfs(r + 1, c, nxt) or #tries down
                dfs(r - 1, c, nxt) or #tries up
                dfs(r, c + 1, nxt) or #tries right
                dfs(r, c - 1, nxt)    #tries left
            ) #tries all 4 directions and starts to recurse that way

            #the undo step we return the board[r][c] variable and tell other searches
            #they can try the cell
            board[r][c] = temp

            return found



        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): #if starting point of r,c didnt work we try the next one
                    return True
                
        return False #if we are here we have tried all starting points none worked


        