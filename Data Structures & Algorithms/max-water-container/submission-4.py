class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        best = 0

        while l < r:
            if heights[l] < heights[r]:
                area = (r-l) * heights[l] 
                print(area)
                if best < area:
                    best = area
                l += 1
            else:
                area = (r-l) * heights[r]
                if best < area:
                    best = area
                r -= 1
        return best
            