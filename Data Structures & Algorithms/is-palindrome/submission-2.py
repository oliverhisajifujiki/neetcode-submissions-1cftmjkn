class Solution:
    def isPalindrome(self, s: str) -> bool:
        #classic two pointer problem as we are considering things at beg / end at the same time
        #initialize l at the start and r at the end
        #while l < r 
            # increment l until it points to proper char
            # decrement r until it points to a proper char
            # if l != r return false else moth pointers l += 1, r -= 1
        #outside return true

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r-=1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True
