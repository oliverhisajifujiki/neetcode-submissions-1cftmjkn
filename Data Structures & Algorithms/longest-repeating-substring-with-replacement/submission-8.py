class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sliceDict = {}
        l = 0
        r = 0
        longest = 0
        while r < len(s):
            c = s[r]
            if c not in sliceDict:
                sliceDict[c] = 0
            
            sliceDict[c] += 1

            while (r - l + 1) - max(sliceDict.values()) > k:
                sliceDict[s[l]] -= 1
                if sliceDict[s[l]] == 0:
                    del sliceDict[s[l]]
                 
                l += 1
            
            #if we are here then we have a valid substring
            if longest < (r - l + 1):
                longest = r - l + 1
            
            r += 1
        return longest

            

