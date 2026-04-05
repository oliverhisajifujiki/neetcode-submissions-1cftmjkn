class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we will use a sliding window to expand along s
        #and checkuntil we have a repeated char 
        #if we have a repeated char we will move one of the endsof the wwindow
        #to the last seen of the repeated char of what we saw 
        #e.g abcdeb this repeated b we take note of , in lastSeen[b] will tell us that index 1 is 
        #where we last saw it, so we move l sliding window to lastSeen[b] + 1
        #new windows becomes cdeb and we keep going 
        #whenever we move window we check if the size of it is larger than best seen 

        lastSeen = {} #key char, and value is the last seen index 
        l = 0
        best = 0
        
        for r in range(len(s)):
            c = s[r] 
            #if c is in our window
                #r > lastSeen[c] > l 
            if c in lastSeen and lastSeen[c] >= l:
                l = lastSeen[c] + 1
            
            lastSeen[c] = r
            windowSize = (r - l) + 1 #if r == l we still have a windowSize of 1
            if windowSize > best:
                best = windowSize
        
        return best
            
            
            


