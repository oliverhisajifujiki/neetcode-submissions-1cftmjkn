class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #we are checking membership often 
        #we should make nums a set
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 in nums:
                continue #x can't be the start of a seq, 
            check = x + 1
            counter = 1
            while check in nums:
                check += 1
                counter += 1
            if best < counter:
                best = counter
        
        return best 
        

