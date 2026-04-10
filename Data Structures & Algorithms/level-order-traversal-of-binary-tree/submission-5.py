# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #BFS VERSION
        #tree empty no levels to return 
        if not root:
            return []
        
        q = deque([root])

        res = []

        while q: #keep going until q is empty

            #q holds this whole levels nodes
            levelSize = len(q)
            
            level = [] #hold all level's node values we will append to res after each level is done

            for _ in range(levelSize):

                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            res.append(level)

        return res
                
            
                

        


