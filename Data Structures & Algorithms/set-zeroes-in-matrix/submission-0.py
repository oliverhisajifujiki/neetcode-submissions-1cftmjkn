class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #the danger is if we just start 0ing we dont know which ones are new / old
        #this matter cause if we dont keep track we will just zero everything

        #so we just go through the matrix once, 
            #put all the rows / colns that we need to zero in a set

        #go through matrix again and 0 the rows and matrices we need to 0

        rows = len(matrix)
        cols = len(matrix[0])

        zeroRows = set()
        zeroCols = set()

        for r in range(rows): #first pass find all 0's
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeroRows.add(r)
                    zeroCols.add(c)
                
        
        for r in range(rows): #actually zero out the rows / cols in our sets
            for c in range(cols):
                if r in zeroRows or c in zeroCols:
                    matrix[r][c] = 0
        