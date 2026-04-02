class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #transpose gets almost all the way to what we want
        #the only step left is reversing each row 
        n = len(matrix)
        #transpose
        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
        
        #reverse each row
        for r in range(n):
            matrix[r].reverse()