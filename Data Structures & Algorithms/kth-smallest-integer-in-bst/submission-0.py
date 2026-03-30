# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #for kth smallest we traverse all the way to the left,
        #push these into a stack
        #once we reach None pop one from the stack pot = stack.pop()
        #this is the smallest integer , k -= 1
        #if k is now 0 return pot
        #else check if theres a right subtree at pot
        #if there is a right subtree and we'd traverse this one all the way to the left

        stack = [] 
        cur = root

        while stack or cur: #traverse / keep popping
            while cur:
                stack.append(cur)
                cur = cur.left #traverse all the way to the left

            #outside of this while we have reached the most left most
            cur = stack.pop()
            k -= 1

            if k == 0: #then whats in cur rn is "kth smallest"
                return cur.val
            
            cur = cur.right #now look at the right subtree
            #if cur is none we skip the inner while
            #and pop another, we keep popping until our counter == 0