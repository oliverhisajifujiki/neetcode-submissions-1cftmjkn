class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #create tDict = {} with keys being the char needed and value is the freq needed
        #windowDict = {} with keys being char in window and value is freq of char in window
        #completed is the number of distinct char that meet the freq needed from t
        #distinct is how many distinct characters there are 
        #we then iterate through l += 1 until s[l] in tDict
        #do for r in range(l, len(s), 1) 
        # add s[r] into windowDict{s[r]} count
        #check to see if  completed needs to be updated
        #once completed == distinct valid window
        #then increment l to see if we can shrink the window 

        completed = 0
        res = [-1, -1] #stores start and stop indices for window
        resLen = float("inf") #this will be how we check if the new res made the length smaller or not 
        tDict = {}
        #populate tDict
        for c in t:
            if c not in tDict:
                tDict[c] = 0
            tDict[c] += 1
        distinct = len(tDict)

        windowDict = {}
        l = 0
        for c in s: 
            if c in tDict:
                break 
            l += 1
        
        for r in range(l, len(s), 1):
            c = s[r] 
            if c not in windowDict:
                windowDict[c] = 0
            windowDict[c] += 1

            if c in tDict and windowDict[c] == tDict[c]: #increment completed if have enough of c in our window 
                completed += 1

            while completed == distinct: #if it is a valid window 
                #update res
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l + 1

                windowDict[s[l]] -= 1

                if s[l] in tDict and windowDict[s[l]] < tDict[s[l]]:
                    completed -= 1
                
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""

            



        