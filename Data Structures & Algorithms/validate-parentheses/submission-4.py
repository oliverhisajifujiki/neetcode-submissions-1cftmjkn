class Solution:
    def isValid(self, s: str) -> bool:
        #we use a dictionary to differentiate between various open and close brackets
        #the use of the dictionary 
            #is if we come across a closed bracket 
                #we then ask what the associated opening bracket should be
        
        #we keep track of a stack of the brackets
        #once we see a closing bracket 
            #we check to see if the stack last element is the corresponding open bracket
                #if not this is not a valid param return false 
                #else we pop the stack
        
        #go along the string like normal 
        
        stack = [] #define stack
        brackDict = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        for c in s:
            if c in brackDict: #this means c is a closing brack
                if not stack or  brackDict[c] != stack[-1]: #checking to see if the last thing we saw was the corresponding open brack if not return false
                    #need the extra check incase the first thing we see is a close brack and stack is empty
                    return False
                #if we are here we know it was the proper match, pop it
                stack.pop()
                
            if c in brackDict.values(): #this is an open brack not super efficient 
                stack.append(c)
        
        return len(stack) == 0 #each corersponding open brack needs a close brack
