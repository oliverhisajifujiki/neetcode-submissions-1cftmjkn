"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #if inputted graph is empty return None
        if not node:
            return None
        #we need a way of marking when we have already copied it
        #and the flow is going to be check if in the orig. graph we hve copied over that node
        #then check if we've copied its neighbors

        #because of this flow a dictionary works nice 
        #where the keys of the dictionary is orig node
        #and the values of the dictionary is copied node
        
        oldToNew = {}
        
        #this is nice because we can then first of all check if we have alr copied say node [x]
        #via:   if x in oldToNew
        #further we can get to the copied neighbors from x easily 
            #via: oldToNew[x].neighbors
        
        def dfs(cur):
            #if we alr cloned cur just return existing copy
            #this is our base case
            if cur in oldToNew:
                return oldToNew[cur]

            #else we have not copied cur yet, therefore copy it
            copy = Node(cur.val)
            oldToNew[cur] = copy

            #next we copy over the neighbours of cur
            for n in cur.neighbors:
                #key is that the neighbor might not be defined yet 
                #this is where we recursively call dfs
                #this is also why in our previous check we simply returned the copy if we alr visited
                copy.neighbors.append(dfs(n))
        
            #here all neighbors have been processed, return the clone
            return copy
    
        return dfs(node)



