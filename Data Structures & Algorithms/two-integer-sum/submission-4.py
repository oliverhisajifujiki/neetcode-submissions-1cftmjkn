class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i in range(len(nums)): 
            n = nums[i]
            check = target - n
            if check in numsDict:
                return [numsDict[check], i]
            if n not in numsDict:
                numsDict[n] = i
            numsDict[n] = i
        