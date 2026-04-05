class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #go through nums, and check to see if target - n has been seen

        nDict = {}

        for i in range(len(nums)):
            n = nums[i]
            m = target - n
            if m in nDict:
                return[nDict[m], i]
            
            if n not in nDict:
                nDict[n] = i 
            
        return []  
            
