class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #the variable continuous substring pulls us into a sliding window solution
        #we want to quickly identify if there is a repeat so we are hashing
        #we do the same sort of thing with l = 0 and r = 1 and best = 0
        #the hashing is key: character value: index where it was last seen
        #we look at the substring s[l:r] check if best < len(s[l:r])
        #if there are no repeats r += 1 
        #if we do have repeats we move l to the next last seen of the newly looked at s[r]
        #this ensures the substring
        #this does mean that we have to update lastSeen[s[r]] later! 
        l = 0
        #r = 1 #defining this outside does not work for empty string
        best = 0
        lastSeen = {}

        for r in range(len(s)):
            #lastSeen[s[l]] = l now because we are just iterating r and r starts from 0
            #we can just look at adding to the dict via lastSeen[s[r]] = r 
            # if s[r] in lastSeen that means we've already observed this char
            # but its okay as long as its not in the slice s[l:r]
            # we know it would be in the slice if the index of the last seen >= l
            # equal is important here for consecutive duplicates "bba"
            if s[r] in lastSeen and lastSeen[s[r]] >= l: #duplicate
                l = lastSeen[s[r]] + 1 #note it still catches if we check "bba.."
            
            lastSeen[s[r]] = r
            if (r - l + 1) > best:
                best = (r - l) + 1
        return best




