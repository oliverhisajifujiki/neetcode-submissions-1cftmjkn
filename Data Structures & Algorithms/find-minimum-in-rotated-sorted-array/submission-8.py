class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = l + r // 2

        while l < r:
            #if we look at the middle and if the middle is < than the last element
            #this has to mean that the ladder half is sorted, and further,
            #the min is in the first half
            if nums[m] < nums[r]:
                r = m
                m = (r + l) // 2
            
            else: #this 
                l = m + 1 
                m = (r + l) // 2
        
        return nums[r]