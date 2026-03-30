# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 #once we reach the leaves and pass on nothing that is not a level we count, the recursion comes back up
        
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right)) #now we add 1 to our levels
        #and then find out if either the left side or right side has more depth
        #which ever one returns the max will give the level of either left or right subtree
        