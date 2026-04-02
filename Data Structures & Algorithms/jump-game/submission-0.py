#we just greedily go along the only nuance is that if 
# the index is farther than what we can possible jump (some farthest value we keep track of)
#at any moment we know to just return false

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #store farthest we can current reach
        farthest = 0

        for i in range(len(nums)):
            if i > farthest: 
                return False
            
            #if we are here its possible to reach this index, therefore update farthest
            farthest = max(farthest, i + nums[i])

        return True
            
