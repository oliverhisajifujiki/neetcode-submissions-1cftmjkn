class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0

        for n in nums:
            if n-1 in nums:
                continue
            
            check = n + 1
            counter = 1
            while check in nums:
                check += 1
                counter += 1
            
            if counter > best:
                best = counter
        
        return best 
