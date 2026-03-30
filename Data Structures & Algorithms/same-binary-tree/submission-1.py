# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
        if not p and not q: #so here we got at the same time that the investigating subtrees are past the leaves
            return True #therefore we know that they end at the same time indicates this is true
        
        if not p or not q: #this only catches if 1 of p or q is past the leaves if both were past the leaves then it would be caught by the above if 
        #we have reached past the leaves at differing times therefore reutrn false
            return False

        if p.val != q.val: #the roots of compared trees are not equal
            return False 
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) #recursive step