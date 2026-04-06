class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #rolling product #we want to keep track 
        n = len(nums)
        res = [1] * n

        lP = 1
        for i in range(n):
            res[i] = res[i] * lP
            lP = lP * nums[i]
        
        rP = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i] * rP
            rP = rP * nums[i]
        
        return res
