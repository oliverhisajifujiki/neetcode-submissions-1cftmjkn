class PrefixTree:
    #a tree where each node is a letter and each path going from one of the child to a leaf is a word
        #you can sometimes think of it as the edges are a character each path from the root spells a prefix

    #quick at inserting words
    #quick at searching for words
    #quick at checking prefixes
    #hash maps are good for full word lookup 
        #trie especially good when prefixes matter
            #autocomplete / spell checker

    def __init__(self):
        #each node in trie stores a dictionary called children
            #key is a character
            #value is another prefix tree node
        self.children = {} #not a binary tree we can lots of children 

        self.endOfWord = False #a flag that says this is the end of the word
        

    def insert(self, word: str) -> None:
        cur = self #self gives you the root

        #go through the word 
        for c in word:
            #if c not in children of cur we are in new territory
            #create a new trienode for it
            if c not in cur.children:
                cur.children[c] = PrefixTree()
            
            #if we are here we know c is a child
            cur = cur.children[c] #and go to the next char

        
        #outside loop we have now gone through the whole word
            #and cur points to the end of the word therefore we can mark it
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        #start at root
        cur = self

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.endOfWord #important check even if we contain the prefix we only return true if it has been marked a word

    
        

    def startsWith(self, prefix: str) -> bool:
        #start at root
        cur = self

        for c in prefix:
            if c not in cur.children: #this means that no word in trie begins with prefix
                return False
            
            cur = cur.children[c]
        
        #if we have reached here we've gone through the whole prefix
        return True
        
        