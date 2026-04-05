class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #go through the window 
        l = 0
        #iterate via shifting r
        #if when we move r we see a repeat s[r] is a problem
            #l must then be shifted to the last time we saw s[r]
            #we will need a dict of last seens
        
        lastSeen = {} #key is char , value is the index it was last seen

        #with this now when we have a repeat at s[r]
            #we shift l such that l = lastSeen[s[r]] + 1
            #therefore this window does not have any repeats

        #only after the shift can we check if this window is a best or not 
        best = 0


        r = 0
        while r < len(s):
            c = s[r]
            #checking if we have seen c before
            #and if we have seen c before check if it is in our window
            if c in lastSeen and lastSeen[c] >= l:
                #we have a duplicate
                l = lastSeen[c] + 1

            #update lastSeen
            lastSeen[c] = r

            windowSize = (r - l) + 1#added one as if l, r same index our window size is still 1

            if windowSize > best:
                best = windowSize
            r += 1
        
        return best





