class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                area = (r - l) * heights[l]
                if best < area:
                    best = area
                l += 1
            
            else: #heights[r] < heights[l]
                area = (r - l) * heights[r]
                if best < area:
                    best = area
                r -= 1
        
        return best 