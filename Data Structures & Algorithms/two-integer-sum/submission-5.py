class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {} #key is the number value is it's index
        #we will go through n in nums
        #check if target - n we've seen alr 
            #if so return index(target - n) , index(n) 
        

        for i in range(len(nums)):
            n = nums[i]
            x = target - n

            if x in numsDict:
                return [numsDict[x], i]
            
            numsDict[n] = i

        return []
            
