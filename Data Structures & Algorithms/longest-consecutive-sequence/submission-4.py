class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        #just go through each one see how long we can go for
        longest = 0
        for x in numSet:
            if x-1 in numSet:
                continue #this is the thing that keeps us at O(n) it ensures we only truly enter this loop once per n in nums
            counter = 1
            check = x
            while check + 1 in numSet:
                counter += 1
                check += 1
            if longest < counter:
                longest = counter

        
        return longest