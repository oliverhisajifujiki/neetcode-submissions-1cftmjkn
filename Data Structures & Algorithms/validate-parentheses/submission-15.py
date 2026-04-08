class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackDict = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        brackSet = set(["(", "[", "{"])

        for c in s:
            if c in brackSet:
                stack.append(c)
            elif c in brackDict:
                if len(stack) == 0 or stack[-1] != brackDict[c]:
                    return False
                #if we are here it matches pop it and move on
                stack.pop()
        return len(stack) == 0
