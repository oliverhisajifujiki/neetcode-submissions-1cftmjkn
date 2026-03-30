class WordDictionary:
    #in the name a dictionary is most natural and fast
        #but whats big is one thing we want to do is allow these "." dots
        #these dots act like wild cards and therefore this is what would make a dictionary veyr hard
        #in this trie if we see a dot we explore all edges

    def __init__(self):
        #dictionary of children where key is letter and value is another trie node
        self.children = {}
        #flag for end of word
        self.flag = False
    
    def addWord(self, word: str) -> None: #this is going to be the exact add as any trie
        #start at root
        cur = self

        #go through the word
        for c in word:
            if c not in cur.children:
                #make it a child
                cur.children[c] = WordDictionary()
            cur = cur.children[c] 
        
        #added the whole word
        cur.flag = True

        

    def search(self, word: str) -> bool:
        
        def dfs(node, i): #takes in a node and how many matching chars so far
            if i == len(word): #we have found a match 
                return node.flag
            
            c = word[i]

            if c != ".": #we are a normal character
                if c not in node.children:
                    return False
                
                #this is the recursive step 
                #note if we are here c is in children therefore we add one to matching chars
                #and we look at the next matched node
                return dfs(node.children[c], i+1)
            
            #if we are here its asking for a wild card
            for child in node.children.values(): #go through all children's nodes
                if dfs(child, i + 1):
                    return True
            
            #if we are here the letter after the wild card is not in our trie
            return False

        #search starting from the root, and we have 0 matching chars now
        return dfs(self,0)
