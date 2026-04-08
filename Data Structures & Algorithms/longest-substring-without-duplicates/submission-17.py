class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0 
        r = 0
        longest = 0
        while r < len(s):
            c = s[r]
            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            
            seen[c] = r

            if r - l + 1 > longest:
                longest = r - l + 1
            
            r += 1
        
        return longest

