class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #the two pointer is not super clear in the beginning for me 
        #but we start at the ends with l and r like normal
        #and we either move l or r in depending on which one is smaller
        l = 0
        r = len(heights) - 1
        best = 0

        while l < r:
            lH = heights[l]
            rH = heights[r]
            area = (r - l)*(min(lH, rH))
            if best < area:
                best = area
            
            if rH < lH:
                r -= 1
            else: 
                l += 1
        return best