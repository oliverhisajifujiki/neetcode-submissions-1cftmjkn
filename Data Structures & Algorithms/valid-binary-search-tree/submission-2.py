# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #can't just compare with the immediate children. 
        #e.g 4 <- 5 (root) -> 6 // 3 <- 6 -> 7 
        #is not a valid BST even though for every node left child less, right child more
        #therefore the right way recursively to do this is every node must lie within an allowed range
        #we pass along left suptree and an upperbound 
        #right subtree and a lowerbound
        def dfs(node, low, high):
            if not node: 
                return True #past the leaves empty tree is a valid BST
            
            if not (low < node.val < high): #outside our bounds
                return False
            
            #now we do recursion
            #the left subtree has the same lower bound
            #but the left subtree must adhere to a new uppper bound 
            #i.e. this nodes value 
            #the right subtree has the same upper bound
            #but the right subtree must adhere to a new lower bound
            #i.e. this nodes value
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("inf"))
        