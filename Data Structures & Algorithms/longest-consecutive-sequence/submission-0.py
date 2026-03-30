class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #essentially we are checking membership of i+1 , then i+2 and seeing how long this can go
        #because we want fast membership checks we are definitly hashing
        #the shortening of runtime is before checking i+1 check i-1 
        #if i-1 is in our set we know i isn't the start of a sequence->dont check i+1
        #good place for a set
        numSet = set(nums)

        longest = 0
        for x in numSet:
            if x-1 in numSet:
                continue
            check = x
            counter = 1
            while check + 1 in numSet:
                counter = counter + 1
                check = check + 1
            if counter > longest:
                longest = counter
        return longest
            
        