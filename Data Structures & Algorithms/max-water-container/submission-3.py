class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #the idea for this 2 pointer is to calculate area 
        #then shift the smaller of heights[l] or heights[r]
        l = 0
        r = len(heights) - 1
        best = 0

        while l < r: 
            area = (r - l) * min(heights[l], heights[r])
            best = max(best, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return best