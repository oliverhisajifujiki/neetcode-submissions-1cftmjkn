class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nDict = {} 
        for i in range(len(nums)):
            x = target - nums[i]
            if x in nDict:
                return [nDict[x], i]
            
            nDict[nums[i]] = i
        
        return []