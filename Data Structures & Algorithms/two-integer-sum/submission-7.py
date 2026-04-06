class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #go through list
        #populate a dict
        #if we have previously seen target - nums[i] 
            #return nDict[target] - i 
        
        nDict ={} #key is the number, value is the index we saw it 
                    #because we want the smallest indices to be returned
                    #if this is alr populated we do not need to overwrite indices
        
        for i in range(len(nums)):
            n = nums[i]
            s = target - nums[i]
            if s in nDict:
                return [nDict[s], i]
            
            if n not in nDict:
                nDict[n] = i
        
        return []