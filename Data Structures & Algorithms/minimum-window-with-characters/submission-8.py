#first we need to define a tDict
    #tDict will be used to check if our window contains all the chars and freq needed
#we then will have a sliding window dict 
    #which will store the char's and their freq 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = {}
        for c in t:
            if c not in tDict:
                tDict[c] = 0
            tDict[c] += 1

        slideDict = {}
        l = 0
        resLen = float("inf")
        res = [-1, -1] #stores the indices of the substring

        #we can not simply check the dicts by doing == to each other we need 1 to keep track of 
        #the distinc chars in t 
        distinct = len(tDict) #this returns the number of keys which is exactly what we want
        completed = 0

        for r in range(l, len(s)):
            c = s[r]
            if c not in slideDict:
                slideDict[c] = 0
            slideDict[c] += 1
            
            if c in tDict and slideDict[c] == tDict[c]: #we have the proper frequency
                completed += 1
                print(c + " is completed")

            while completed == distinct: #we have a valid substring (may not be smallest)
                #we may have a smallest window
                print(s[l:r + 1])
                window = r - l + 1
                if window < resLen:
                    resLen = window
                    res = [l, r]
                #now we have to check if we can keep moving l to the right
                leavingChar = s[l]
                slideDict[leavingChar] -= 1
                l += 1

                if leavingChar in tDict and slideDict[leavingChar] < tDict[leavingChar]: #we removed a necessary char and now aren't a proper substring
                    completed -= 1

        if resLen == float("inf"): #we never got a matching substring
            return ""
        #if we are here we did find a substring
        return s[res[0]: res[1] + 1]


        
