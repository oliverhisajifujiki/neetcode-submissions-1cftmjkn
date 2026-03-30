class Solution:
    def findMin(self, nums: List[int]) -> int:
        #in order to run this in log(n) usually it means at each step we are "throwing away"
        #about half of the probable values
        #the classic is to pick the middle of the list and decide which half contains the min
        #key comparison is usually the right end
        #if mid > last then we know that it restarted in this later end therefore the min is there
        #else the min is in the first half

        #init with l = 0 r = len(nums) - 1 , mid = (r + l) // 2
        
        l = 0
        r = len(nums) - 1
        m = (r+l) // 2

        while l < r:
            if nums[m] > nums[r]:
                l = m + 1
                m = (l + r) // 2
            else:
                r = m
                m = (l+r)//2

        return nums[l]
