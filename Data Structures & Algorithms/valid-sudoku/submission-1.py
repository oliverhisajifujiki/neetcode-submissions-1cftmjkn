class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #there are 3 sorts of sets to keep in mind 
        #the columns / rows / squares
        #if we are checking the validity of element i in the sudoku table
        #we check if i appears again in it's coln / row / square
        #this is checking membership fast therefore we know we will be employing hash
        #so for each row and for each column and each grid we save a hash
        # we will have 27 hashes 
        #the route can be find the next non empty cell say its element (i,j)
        #check if we have calculated a hash for row i coln j and the grid its in
        #grid it is in is more complicated, but we just take the quotient (excluding the remainder) of i and j
        #this is calculated by i//3 and j//3 this pairwise will uniquely identify which grid we are in

        #we know that this is always a 9x9 board
        rowDict = {}
        colDict = {}
        gridDict = {}

        for i in range(9):
            for j in range(9):
                g = (i//3,j//3) #grid index
                val = board[i][j]
                if val == ".": #means empty cell
                    continue #check next element 
                
                if i not in rowDict: #check the row hash
                    rowDict[i] = {val}
                else:
                    if val in rowDict[i]:
                        return False
                    rowDict[i].add(val)

                if j not in colDict: #check coln hash
                    colDict[j] = {val}
                else:
                    if val in colDict[j]:
                        return False
                    colDict[j].add(val)

                if g not in gridDict: #check grid hash
                    gridDict[g] = {val}
                else:
                    if val in gridDict[g]:
                        return False
                    gridDict[g].add(val)
        return True

                


        