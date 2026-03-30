class Solution:
    def isValid(self, s: str) -> bool:
        #we will have a stack that stores the brackets we see
        #if we see an opening bracket push it into the stack
        #if we see a closing bracket we check the stack
        #make sure the top of the stack is an opening bracket that matches the closing bracket
        #we will use a dictionary to easily match the closing bracket with an opening one
        #the key will be the closing bracket e.g. "]" and the value will be the corresponding open "["

        stack = []
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        
        #go through the string check if the current char is a bracket 

        for c in s:
            if c in closeToOpen:
                if not stack or stack[-1] != closeToOpen[c]: #check if the stack is empty or if the latest seen opening bracket matches this closing one
                    return False
                stack.pop()
            elif c in closeToOpen.values():
                stack.append(c)

        return len(stack) == 0    


