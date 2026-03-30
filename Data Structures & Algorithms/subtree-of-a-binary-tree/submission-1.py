# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #because an empty tree is a subtree of any tree if subRoot is None we return false
        if not subRoot:
            return True
        
        #if we are past the first if , we know subRoot is not empty
        if not root: #therefore if subRoot is not empty and the root is we can't be a subtree
            return False
        
        #now we know neighter are empty
        #check the two trees are equal
        if self.isSameTree(root, subRoot):
            return True
        
        #if we got here the two trees we got are not equal, lets check left and right children of bigger tree
        #recursive call
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def isSameTree(self, p, q):
        if not p and not q: #both are empty
            return True
        if not p or not q: #because of first if statement we know one of p and q is nonempty
        #therefore if we enter only 1 is empty
            return False
        if p.val != q.val:
            return False #passed through root value is not equal
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        