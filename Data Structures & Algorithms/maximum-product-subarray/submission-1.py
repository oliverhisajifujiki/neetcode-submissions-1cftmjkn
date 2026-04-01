class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #going along we keep track of both the min and the max 
        #the min is useful just in case at element i is a negative number
        #turns the min into a max

        res = nums[0]
        curMax = 1
        curMin = 1

        for n in nums:

            #for each n we simply test if n itself is the min/max or n*curMax or n*curMin

            #holder variable for curMax*n as we will overwrite curMax on first comparison
            tmp = curMax * n

            curMax = max(n, n * curMax, n * curMin)
            curMin = min(n, tmp, n * curMin)

            res = max(res, curMax)

        return res