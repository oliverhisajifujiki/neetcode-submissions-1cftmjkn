# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #two choices at a node
            #return upward to parent
            #global answer is here
        
        #for a node a path can use
            #just the node
            #node + left subtree
            #node + right subtree
            #node + left subtree + right subtree
        
        #BUT when returning upward to the parent , you can not return both left and right 
            #would give a branch

        #the idea is we go all the way down the tree and we ask
            #what is the best single path starting at this node that i can return to parent
            #what is the best path that passes through this node the overall best so far
        
            #the first question we can only return either left or right
            #the second one the path would go from left -> node -> right

        best = float("-inf")

        def dfs(node):
            nonlocal best #global best

            if not node: #base case 
                return 0 #past the leaves the value is 0
            
            leftGain = dfs(node.left) #recusively go down
            rightGain = dfs(node.right)

            #if child path is negative ignore it just 
            leftGain = max(leftGain, 0)
            rightGain = max(rightGain, 0)

            #checking to see if best path sum goes through this node
                #meaning that this node is the "highest" point
                    #would include left branc + current node + right branch
            throughNode = node.val + leftGain + rightGain

            #update the best global if this through path is better
            best = max(best, throughNode)

            #okay so we have saved if we want the bath to be both subtrees
            #the other option is whether return left subtree or right subtree
            #note we can return none! that is saved in the gain = max()
                #if we return 0 there its the same as not returning a subtree
            return node.val + max(leftGain, rightGain)
        
        dfs(root) #start from the root

        return best
            


