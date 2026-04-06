class Solution:
    def isPalindrome(self, s: str) -> bool:
        #pointer for beginning 
        #pointer for end
        l = 0
        r = len(s) - 1

        while l < r:
            #only compare alpha numerics
            while l < r and not s[l].isalnum():
                l += 1
            
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            #they do equal increment next 
            l += 1
            r -= 1
        
        return True