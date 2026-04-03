class Solution:
    def isPalindrome(self, s: str) -> bool:
        #we just go from the start and end (2pointers)
        #only weird thing is we ignore non alphanum. char

        l = 0
        r = len(s) - 1

        while l < r:
            #make sure we are comparing only alphanum
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True