# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        #dfs 
        def dfs(node, depth): #this function takes in the node,
                                #it will record its value in a list 
                                #this list will hold all values of the tree with that particular depth
            if not node:
                return None #nothing to record
            
            if len(res) == depth: #as we start depth at 0, this means there actually isn't enough lists
                res.append([])

            res[depth].append(node.val)
        
            dfs(node.left, depth + 1) #we are going down the tree
            dfs(node.right, depth + 1) #this order is important here because they want left to right

        dfs(root, 0) #again we are starting at depth 0 for the root

        return res
        


