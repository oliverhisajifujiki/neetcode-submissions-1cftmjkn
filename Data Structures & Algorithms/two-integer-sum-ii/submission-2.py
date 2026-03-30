class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #as we are sorted this works well for two pointer 
        #the reason for this is if we have l and r again
        #check their sum if its too small we know we want l += 1
        #if sum is too big we do r -= 1
        #else we return the indices
        l = 0
        r = len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1,r + 1]
            if s > target:
                r -= 1
            else:
                l += 1
            
            

        