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
        
        #
        q = deque([root]) 

        res = []

        while q:
            #q holds this levels nodes
            levelSize = len(q)
            level = []

            for _ in range(levelSize):
                #look at next node
                node = q.popleft()
                #record its value into level

                level.append(node.val)

                #now we want to populate q with the next level
                if node.left:
                    q.append(node.left)


                if node.right:
                    q.append(node.right)
            
            #once we are here we went through the whole level
            res.append(level)
        
        return res
                
            
                

        


