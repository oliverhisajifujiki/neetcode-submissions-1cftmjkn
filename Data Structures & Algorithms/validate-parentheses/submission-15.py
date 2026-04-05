class Solution:
    def isValid(self, s: str) -> bool:
        #stacks have stack.append(x) this pushes x
        #stack.pop() 
        #stack[-1] is a peak

        stack = []

        brackDict = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        openSet = set(["{", "(", "["])

        for c in s:
            if c in openSet:
                stack.append(c)
            elif c in brackDict:
                if not stack or stack[-1] != brackDict[c]:
                    return False #wrong bracket ordering
                #we have matching brackets! pop
                stack.pop()
        
        return len(stack) == 0

                