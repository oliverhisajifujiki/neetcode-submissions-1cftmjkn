# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #if both p and q are smaller than current node (p,q are in left subtree)
        #go left
        #if both p and q are bigger (p,q are in right subtree)
        #go right
        #else this is actually where they are split therefore this is LCA 

        #instead of recursive we assign the root to a holder var cur
        cur = root

        while cur: #if this is false we went past 
            if p.val < cur.val and q.val < cur.val: #both p and q are smaller that cur node
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val: #both are larger
                cur = cur.right
            else:
                return cur
        
        return None
