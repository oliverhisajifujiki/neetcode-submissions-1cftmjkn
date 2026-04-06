class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: #we alr calculated a 3sum's for nums[i - 1] 
                #                                   if we are equal to that we will just be calc dupes
                continue
            
            targ = nums[i] #pseudo target we want -targ = a + b
            l = i + 1
            r = n - 1
            while l < r:
                s = targ + nums[l] + nums[r]

                if s == 0:
                    res.append([targ, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1 #no need to even check dupes
                    
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1
                
                elif s > 0: #sum too big as we are sorted shift r
                    r -= 1
                    while l < r and nums[r + 1] == nums[r]:
                        r-=1
                
                else: #s < 0 too smaall so we shift l
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        return res
                    
