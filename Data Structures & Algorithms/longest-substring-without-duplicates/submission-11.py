class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #going along we start with the first character i = 0 s[i]
        #count how long until you can get to a repeated character
        #each time you go to a next char interate a counter j 
        #if we hit a repeat at s[j] we set i to be lastSeen[s[j]]

        #therefore most useful to have a dictionary of key : char and val : last index of char

        lastSeen = {}
        l = 0
        best = 0

        for r in range(len(s)):
            c = s[r]
        
            #check if we have seen c within l -> r (window we are considering)
            if c in lastSeen and lastSeen[c] >= l: #duplicate
                l = lastSeen[c] + 1 
            
            lastSeen[c] = r
            if (r - l + 1) > best:
                best = (r - l + 1)
            
        return best
