class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = {}

        for c in t:
            if c not in tDict:
                tDict[c] = 0
            
            tDict[c] += 1
        
        completed = 0
        distinct = len(tDict)
        resLen = float("inf")
        res = [-1, -1]
        sliceDict = {}

        l = 0
        r = 0
        while r < len(s):
            c = s[r]
            if c not in sliceDict:
                sliceDict[c] = 0
            sliceDict[c] += 1

            if c in tDict and tDict[c] == sliceDict[c]: #we have the correct amount
                completed += 1
            
            while completed == distinct: #we have a valid substring
                windowSize = r - l + 1
                if windowSize < resLen:
                    res = [l, r]
                    resLen = windowSize
                
                #we are going to shrink the window and see if it has changed things 
                sliceDict[s[l]] -= 1
                if s[l] in tDict and sliceDict[s[l]] < tDict[s[l]]:
                    completed -= 1

                l += 1
            r += 1
            
        if resLen == float("inf"):
            return ""
        return s[res[0]: res[1] + 1]




            




