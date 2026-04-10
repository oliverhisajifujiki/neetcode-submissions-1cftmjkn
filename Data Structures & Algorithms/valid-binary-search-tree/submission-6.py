# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #vist every node make sure this node adheres to bst rule

        #therefore dfs is good for this task
        def dfs(node, low, high):
            if not node:
                return True
            val = node.val
            if not (low < val <  high):
                return False 
            
            return dfs(node.left, low, val) and dfs(node.right, val, high)
            #the left node now must be less than the parent (rules for bst)
            #the right child now must be more than the parent (rules for bst)
        
        return dfs(root, float("-inf"), float("inf"))