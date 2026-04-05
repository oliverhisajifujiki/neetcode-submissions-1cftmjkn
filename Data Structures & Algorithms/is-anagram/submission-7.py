class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #populate a tDict and sDict simply compare them
        sDict = {}
        for c in s:
            if c not in sDict:
                sDict[c] = 0
            sDict[c] += 1
        

        tDict = {}
        for c in t:
            if c not in tDict:
                tDict[c] = 0
            tDict[c] += 1
        
        return sDict == tDict