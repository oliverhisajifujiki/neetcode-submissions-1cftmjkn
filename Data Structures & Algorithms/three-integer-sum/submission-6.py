class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #really hard to get all tuples
        #we have to sort nums
        nums.sort()
        res = []
        n = len(nums)
        #we then go through each n in nums, and now n is the target        
        for i in range(n):
            target = nums[i]
            if i > 0 and target == nums[i-1]:
                continue #if we are the same as previous we alr calculated all the sums, so lets go next
            l = i + 1
            r = n - 1

            while l < r:
                s = target + nums[l] + nums[r]
                if s == 0:
                    res.append([target, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                    
                elif s < 0: #our sum is too low as we are sorted shift l
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                
                else: #sum is too high shift r
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            
        return res


            
            
            

        