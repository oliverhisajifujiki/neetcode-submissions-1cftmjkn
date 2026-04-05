class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        m = (l + r) // 2

        while l < r:
            if nums[r] < nums[m]:
                #this means the min will be in the ladder half of the array
                l = m + 1 #as we have checked that nums[m] is not min we can iterate past it
                m = (l + r) // 2
            else: 
                #this means the min will be in the first half of the array
                r = m 
                m = (l + r) // 2
            
        return nums[r]
            