# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #we must go all the way down and compare values 
        if not p and not q: #both are none these are equal
            return True #most likely our recursion is done as we are past the leaves (or they inputted to empty trees)
    
        if not p or not q: #if we are here because of the first if statement it can't be the case the both p and q are nonempty
            return False #therefore it must be the case that one of the trees is empty and the other isnt
        
        #check if these values are different
        if p.val != q.val:
            return False 
        
        #pass on the left and right subtrees

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)