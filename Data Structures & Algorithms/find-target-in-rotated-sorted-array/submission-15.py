class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #one side is always sorted, if we know its sorted we know if our target lies in this half

        l = 0
        r = len(nums) - 1
        m = (l + r) // 2

        #while loop through it all 
        while l <= r:
            #check if m is the target
            if target == nums[m]:
                return m
            #check if first half is sorted
            if nums[l] <= nums[m]: #if this is the case it must be sorted
                if nums[l] <= target < nums[m]: #we are in the sorted half
                    r = m - 1 #we have alr checked m 
                    m = (l + r) //2
                else: #target is in second hafl
                    l = m + 1
                    m = (l + r) // 2
            else: #if we are here the second half is sorted
                if nums[m] < target <= nums[r]: #we are in the sorted second half
                    l = m + 1
                    m = (l + r ) // 2
                else:
                    #target is in the first half
                    r = m - 1
                    m = (l + r) // 2
        
        return -1
            

                    