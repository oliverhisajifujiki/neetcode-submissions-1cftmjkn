class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        longest = 0 
        sliceDict = {} #just the freq , in the  slice
                        #this will mean though if something leaves the dictionary we will have to delete it

        for r in range(len(s)):
            c = s[r]
            
            if c not in sliceDict:
                sliceDict[c] = 0
            sliceDict[c] += 1

            
            while r-l+1 - max(sliceDict.values()) > k:
                #if we are here not valid slice we have to shift l
                #but when we shift l we must change the freq of our sliceDict
                sliceDict[s[l]] -= 1
                if sliceDict[s[l]] == 0:
                    del sliceDict[s[l]]

                l += 1
            

            if r - l + 1 > longest:
                longest = r - l + 1
            
        return longest