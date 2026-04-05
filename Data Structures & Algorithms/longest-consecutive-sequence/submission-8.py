class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) 
        longest = 0
        for x in numSet:
            #biggest time save
            if x-1 in numSet: #if this is the case we know that x is not the start 
                #of a consecutive sequence so skip
                continue
            #if we got here now just check if x+1 is in set
            check = x + 1
            counter = 1
            while check in numSet:
                counter += 1
                check += 1
            if counter > longest:
                longest = counter

        return longest