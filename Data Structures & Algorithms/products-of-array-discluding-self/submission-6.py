class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        leftProduct = 1

        for i in range(n):
            res[i] = res[i] * leftProduct
            leftProduct = leftProduct * nums[i]
        
        rightProduct = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * rightProduct
            rightProduct = rightProduct * nums[i] 
        
        return res
