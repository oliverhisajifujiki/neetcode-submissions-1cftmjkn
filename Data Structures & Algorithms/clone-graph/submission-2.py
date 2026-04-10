"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        #old to new dictionary
        #key is original node
        #value is copied node
        oldToNew = {}

        def dfs(cur): #dfs is going to be used to get all the nodes neighbours
            if cur in oldToNew:
                return oldToNew[cur] #return the copy
            
            #if we are here it wasn't alr in dictionary lets add 
            copy = Node(cur.val)
            oldToNew[cur] = copy

            for n in cur.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
            
        return dfs(node)

            

