class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        i = 0
        res = []
        while i < n:
            while i < n-1 and i > 0 and nums[i] == nums[i-1]:
                i += 1
            targ = nums[i]
            l = i + 1
            r = n - 1

            while l < r:
                s = targ + nums[l] + nums[r]
                if s == 0:
                    res.append([targ, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif s > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                
                else:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            i += 1
        return res
