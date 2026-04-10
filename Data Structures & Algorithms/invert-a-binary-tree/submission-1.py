# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        #this will return the left subtree that is inverted
        self.invertTree(root.right)
        #this will return the right subtree that is inverted

        return root

