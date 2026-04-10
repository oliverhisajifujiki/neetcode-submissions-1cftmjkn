# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: #both are none! 
            return True #this is checking if we've reached past the leaves at the same time
        
        if not p or not q: #as both none is covered above this check is only entered if 
                            #exactly one of thse are None therefore they arent equal
                            #as one tree reached past their leaves first (one is none)
            return False

        if p.val != q.val:
            return False #we also need to check their values are equiv

        #we check if leftsubTree and right subtree are the same 
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)