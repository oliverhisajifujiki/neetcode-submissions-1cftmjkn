class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #populate the dictionary
        #we can inline check if target - nums[i]
        #is in the dictionary alr
        #we have to return the indices 
        #so dic will be key value of 
        numDict = {}
        #need ind counter
        i = 0
        for n in nums:
            #check if we have alr seen the sum we want
            if target - n in numDict:
                return [numDict[target-n],i]
            
            if n not in numDict:
                numDict[n] = i
            
            
            i += 1
