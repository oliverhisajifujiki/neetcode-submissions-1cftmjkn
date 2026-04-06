class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        best = 0

        while l < r:
            if heights[l] < heights[r]:
                h = heights[l]
                area = (r - l) * h
                if area > best:
                    best = area
                l += 1

            else: #h[r] < h[l]
                h = heights[r]
                area = (r - l) * h
                if area > best:
                    best = area
                r -= 1
        
        return best
