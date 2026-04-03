class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #checking to see if both s and t 
        #have the same freq of each char.
        #use dict because we have to check 
        sDict = {}
        tDict = {}
        for c in s:
            if c not in sDict:
                sDict[c] = 0
            sDict[c] += 1
        
        for c in t:
            if c not in tDict:
                tDict[c] = 0
            tDict[c] += 1
        return sDict == tDict