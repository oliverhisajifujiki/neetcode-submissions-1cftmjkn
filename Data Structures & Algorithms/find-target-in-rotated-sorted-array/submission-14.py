class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #should be the same as finding the min except how we decide what to throw away
        #the comparison would be we are looking at nums[l],nums[m],nums[r]
        #one key thing is no matter how its been rotated one half must be sorted
        #the check would be if nums[l] < nums[m] then 1st half sorted
        #   if nums[m] < nums[r] then 2nd half is sorted
        #   or just else it
        #for whichever side its sorted we ask is target in the sorted half
        #if yes throw away the other half 
        #   else throw away the sorted half

        l = 0
        r = len(nums) - 1
        m = (r + l) // 2

        while l <= r:
            if nums[m] == target:
                return m

            if nums[l] <= nums[m]: #first half is sorted
                if nums[l] <= target < nums[m]: #target is in sorted half
                    r = m - 1
                    m = (r+l)//2
                    print(nums[l:r], "1")
                else: #target is in unsorted half
                    l = m + 1
                    m = (r+l)//2
                    print(nums[l:r], "2")
            else: #second half is sorted
                if nums[r] >= target > nums[m]: #target is in sorted half
                    l = m + 1
                    m = (r+l)//2
                    print(nums[l:r], "3")
                else: #target is in unsorted half 
                    r = m - 1
                    m = (r+l)//2
                    print(nums[l:r], "4")

        return -1     
                



