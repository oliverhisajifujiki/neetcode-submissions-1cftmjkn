# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #the idea here is we go through each level (starting from root)
        #we record this levels values 
        #and we push all the children from this levels value into a queue
        if not root:
            return []
        
        q = deque([root]) #this is all the nodes of this level
        res = []

        while q:
            levelSize = len(q)
            level = []

            for _ in range(levelSize):
                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                
            res.append(level)
        return res



