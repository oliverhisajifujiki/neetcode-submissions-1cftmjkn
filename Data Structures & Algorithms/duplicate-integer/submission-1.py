class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n:
                if nums[i]==nums[j]:
                    return True
                j = j+1
            i = i+1
        return False