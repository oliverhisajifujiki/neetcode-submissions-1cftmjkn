class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        lastSeen = {} 
        longest = 0

        for r in range(len(s)):
            c = s[r]
            if c in lastSeen: #we have seen this, check if it is our window
                if lastSeen[c] >= l: #it is in our window
                    #to ensure we don't have a repeate we assign l = lastSceen[c] + 1
                    l = lastSeen[c] + 1
            
            #now lastSeen[c] can be updated
            lastSeen[c] = r
            #if we are here we do not have a repeat therefore valid substring check if window is the longest
            windowSize = (r - l) + 1
            if longest < windowSize:
                longest = windowSize

        return longest
            
            
