class Solution:
    def longestPalindrome(self, s: str) -> str:
        #the idea is we start at a index i, and we expand from that "center"
        #for example start at s[i] (single char so it is a palindrome)
            #then check if s[i-1] == s[i+1] (start of a valid palindrome)
        
        #the issue is there are "two" types of palindrome tho whether we are odd or even
        #odd palindrome the middle char doesn't need to match anything e.g. "aabaa"
        #even palindrome the middle chars have to match eg "aabbaa"

        #the pattern will be for i in range(len(s)) we consider both an even or odd
            #palindrom starting from i.
            #so as long as l , r stay in bounds , we shift l left and r right till palindrome breaks

        #for odd start with l = i-1 and r = i+1 and check then exapnd 
        #for even start with l= i and r = i+1 and check then expand
        res = s[0] #init this to be the first char #if there is no nontrivial palindrome this will be longest
        resLen = 1

        for i in range(len(s)):
            #odd length
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: #ensures we are in bounds and palindrome condition holds
                if (r-l+1) > resLen: #check if valid palindrome is longer than our current best
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            #even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: #ensures we are in bounds
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                
                l -= 1
                r += 1
            
        return res 
        