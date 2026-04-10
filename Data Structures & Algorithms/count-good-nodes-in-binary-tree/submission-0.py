# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxVal = float("-inf")


        goodCounter = 0
        def dfs(node, maxVal, counter):
            if not node:
                return 
            
            if maxVal <= node.val:

                counter+=1
                print(counter, maxVal, node.val)
                maxVal = node.val
                

            if node.left:
                counter = dfs(node.left, maxVal, counter) 
            
            if node.right:
                counter = dfs(node.right,maxVal, counter)
            #we have no more children
            
            return counter
            
        goodCounter = dfs(root, maxVal,goodCounter)

        return goodCounter

        

