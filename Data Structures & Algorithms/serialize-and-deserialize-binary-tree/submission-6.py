# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #store pre order root left right
        #but whenever there's a gap we must record "N" 
        ser = []

        def dfs(node):
            #okay if get None back we are past a leaf return "N"
            if not node:
                ser.append("N")
                return

            ser.append(str(node.val)) #preorder puts root first

            dfs(node.left) #recursive calls
            dfs(node.right)

        dfs(root) #start from the root

        return ",".join(ser) #makes , the deliminator #must be this way because we want to return a str

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #we got a string, we split it back into tokens
        vals = data.split(",")

        #this index tells us which tocken we are currently reading
        self.i = 0

        def dfs():
            #if the current token is "N", that means this child is missing
            if  vals[self.i] == "N":
                self.i += 1
                return None
            
            #else the token is a real node value
            node = TreeNode(int(vals[self.i]))

            #move to next token
            self.i += 1

            #because we are preorder we do left first and then right
            #the self.i is keeping track so dfs doesn't need an argument
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
