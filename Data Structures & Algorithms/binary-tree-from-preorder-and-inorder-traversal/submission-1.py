# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder is root left right
        #inorder is left root right
        #so preorder will immediately tell us the root we then look at inorder until we see the root this is our left subtree
        if not preorder or not inorder:
            return None #either preorder or inorder is empty we are done looking

        #get the root
        rootVal = preorder[0]
        root = TreeNode(rootVal)

        mid = inorder.index(rootVal) #this defines the left and right subtree 

        root.left = self.buildTree(preorder[1: 1 + mid], inorder[:mid])
        root.right = self.buildTree(preorder[1 + mid:], inorder[mid+1:])

        return root