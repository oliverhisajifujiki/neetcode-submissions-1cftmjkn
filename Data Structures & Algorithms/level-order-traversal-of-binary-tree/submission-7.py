# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #DFS version
        res = []

        def dfs(node, depth):
            if not node:
                return None

            if len(res) == depth: #because we are starting at depth = 0,
                                    #if they are equal we actually do not have enought lists
                res.append([])
            
            #we have the lits for this depth we are happy to insert
            res[depth].append(node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)


        dfs(root, 0)
        return res


