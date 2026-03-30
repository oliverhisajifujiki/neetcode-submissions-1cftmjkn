# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS needs a way to deque the root not a fan
        #DFS, instead of queueing we use recursion and pass the current depth
            #at each node: if first depth visit, create a new list for that level
            # add the node's value to the list 
            # recursively explore the left and right children with depth + 1 

        res = [] #this will be what we return (list of lists)

        #now use make a dfs that takes in both the node and depth we are at
        def dfs(node, depth):
            if not node: #we are past the leaves
                return None
            if len(res) == depth: # we will define the fist depth to be 0 so if we are equal this means that we do not have a list yet for the current depth we are at
            #i.e. this is the first node we are visiting of this depth
                res.append([])
            
            res[depth].append(node.val) # add value to the proper depth
            
            #now the recursive calls left and right children with one higher depth
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root,0) #start the algorithmic call with root at depth 0
        return res