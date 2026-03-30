# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #classic recursive algorithm
        #go all the way down to the leaves (even past the leaves so that we pass None)
        if not root: #again this means we passed None into itself
            return None
        
        #swap the left and right children
        root.left, root.right = root.right, root.left

        #recusively invert the left subtree then the right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        