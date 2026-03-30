class TrieNode:
    def __init__(self):
        self.children = {} #dictionary of children
        #self.flag = False #flag for if a word ends here or not
        #instead of the normal flag because we want to return the word into a list 
            #we have a flag that is None if no word ends here 
            #or the word if it does end there
                #this way we can just return the flag to our res
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #put all the words into a Trie
        #explore the board once with DFS 
            #check if board is in current trie node's children
                #if not stop go to next board char
                #else move into that trie child (c)
                    #if c completes a word record it
                    #mark board cell visited
                    #recurse in 4 directions
                #restore board cell
        
        #build trie from words
        root = TrieNode()

        for s in words:
            cur = root #set cur to root
            for c in s:
                if c not in cur.children:
                    # add it to the tree
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            #now we have added the word s
            cur.word = s #marks the end of a word and stores the word for easy return
        #now we have added all the words

        #now we do DFS on the board
        #what we return is a list of the words we found on board
        res = []
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c,node): #r: row indes, c: col index, node is current node of trie
            #check if we are out of bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            char = board[r][c] #what we are considering right now 

            if char not in node.children: #the candidate board cell not compatible
                return
            
            #if we are here we know that the candidate board cell is in the right direction
            #first we check if including up until (r,c) we have completed a word if so we store it 
            nextNode = node.children[char]

            if nextNode.word is not None: 
                res.append(nextNode.word) #this is why the special flag is nice
                nextNode.word = None #does mean the trie can't be re-used but ensures we don't record duplicates
            
            #mark visited
            board[r][c] = "#"

            #explore neighbours recursive calls
            dfs(r + 1, c, nextNode) #explores down cell
            dfs(r - 1, c, nextNode) #explores up cell
            dfs(r, c + 1, nextNode) #explores right cell
            dfs(r, c - 1, nextNode) #explores left cell

            #if we are here we've gone all the way down now we backtrack i.e. unmakr board
            board[r][c] = char
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root) #starts the call here
        
        return res



                    