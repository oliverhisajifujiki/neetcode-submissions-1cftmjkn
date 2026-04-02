class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #classic dicionary question 
        #go through the list 
        #put in dictionary 
        #check if we are alr in dictionary or not
        
        seen = {}

        for n in nums:
            if n in seen:
                return True
            seen[n] = True

        return False