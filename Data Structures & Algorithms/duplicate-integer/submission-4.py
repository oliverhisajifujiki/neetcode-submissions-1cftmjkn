class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #this time i will use a dictionary as this is the most normal thing personally for me when i think of hash functions
        seen = {} #create a dictionary, where the key is going to be the value in nums and the value will be either true or false

        for num in nums:
            if num in seen:
                return True #this can all remain the same 
            seen[num] = True
        return False    
        