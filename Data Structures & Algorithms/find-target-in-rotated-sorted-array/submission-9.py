class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #the key fact here that we use is no matter how many times we have rotated one half of the array must be sorted
        
        l = 0 
        r = len(nums) - 1
        m = (l + r) // 2

        while l <= r:
            if nums[m] == target:
                return m
            
            #find which side is the sorted 
            if nums[l] <= nums[m]: #first half is sorted 
                if nums[m] > target >= nums[l]: 
                    #target is inside sorted half! 
                    r = m - 1 #alr checked m
                    m = (l + r) // 2
                
                else: #target is inside unsorted half:
                    l = m + 1
                    m = (l + r) // 2
            else: #second half is sorted
                if nums[m] < target <= nums[r]:
                    #target is in sorted half
                    l = m + 1
                    m = (l + r) // 2
                else:
                    #target is in unsorted half
                    r = m - 1
                    m = (l + r) // 2    
        return -1
                    