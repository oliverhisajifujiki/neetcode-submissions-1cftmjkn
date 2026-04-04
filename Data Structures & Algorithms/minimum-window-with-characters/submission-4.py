#prelim
    #whats clear here is we are checking members freq. dicts will be used 
    #will have a tDict
        #where key will be char 
        #and value will be freq
    
    #we will keep track of a windowDict
        #for s[l:r] we will keep track of a similar kind of dictionary

    #the hard part is we need minimum
        #so even if we get a proper substring we have to still go through the whole string
        #to make sure we don't have a smaller substring
        #this is where the logic is hard
        
        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #populate tDict
        tDict = {}
        for c in t:
            if c not in tDict:
                tDict[c] = 0
            tDict[c] += 1
        
        res = [-1, -1] #store the indices of the substring
        resLen = float("inf")
        
        distinct = len(tDict) #this will be a comparison tool
        completed = 0 #we compare this to distinct 
                        #we iterate completed (or minus) when we have enough char freq (matching t)
        
        l = 0
        for c in s:
            if c in tDict:
                break
            l += 1
        
        #this gets us to a proper pointer that actually starts our substring with something in t

        windowDict = {}

        for r in range(l, len(s), 1):
            c = s[r]
            #put it into windowDict
            if c not in windowDict:
                windowDict[c] = 0
            windowDict[c] += 1

            #next check to see if c is in t and if windowDict[c] == tDict[c] 
                #if so then we can increment completed
            
            if c in tDict and windowDict[c] == tDict[c]:
                completed += 1
            
            while completed == distinct: #this is a valid substring
                #update res if this substring is smaller
                
                if r - l + 1 < resLen: 
                    res = [l,r]
                    resLen = r - l + 1
                
                leavingChar = s[l]
                #now we want to increment l and move along the substring to see if we can get antying smaller
                l += 1
                windowDict[leavingChar] -= 1

                #changed our window see if we need to change completed
                if leavingChar in tDict and windowDict[leavingChar] < tDict[leavingChar]:
                    completed -= 1
                    #this will get us out fo this while loop
            
        if resLen == float("inf"): #if this is the case we never got a valid substring   
            return ""
        
        else:
            return s[res[0]:res[1]+1] 

                
                
            

        




        