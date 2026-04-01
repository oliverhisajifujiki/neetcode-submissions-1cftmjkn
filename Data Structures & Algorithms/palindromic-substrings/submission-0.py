class Solution:
    def countSubstrings(self, s: str) -> int:
        #the exact same logic as longestPalindromic substring, 
        #except whenever there is an accepted palindrom in our while loop (inside the for loop)
        #we increment a counter 

        #our init is slightly different, instead of trying to just skip the trivial 1 length substring
        count = len(s)

        for i in range(len(s)):
            #odd length
            l, r = i - 1 , i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: #ensures we are in bounds and palindrome condition holds
                count += 1
                l -= 1
                r += 1
            
            #even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: #ensures we are in bounds
                count += 1                
                l -= 1
                r += 1
            
        return count
        