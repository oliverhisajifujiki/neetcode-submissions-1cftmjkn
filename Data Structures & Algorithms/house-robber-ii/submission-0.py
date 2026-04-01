class Solution:
    def rob(self, nums: List[int]) -> int:
        #edge case n = 1 no circle
        if len(nums) == 1:
            return nums[0]
        
        #after this base case it is exactly the same question as the first robber
            #EXCEPT we either consider:
                #case 1: rob houses [0 ... n-2]
                #case 2: rob houses [1 ... n-1]
        
        return max(self.robI(nums[:-1]), self.robI(nums[1:]))
    
    def robI(self, nums: List[int]) -> int:
        #same logic as robber I

        #rob1 = best answer up to house i-2
        #rob2 = best answer up to hosue i-1
        rob1 = 0
        rob2 = 0
        #instead of recursive though this is the rolling count / array look through
        for num in nums:
            #if we rob this house, total is:
                #current house value + best up to i-2 (which is rob1)
            take = num + rob1

            #if we skip this house, best up to i-1
            skip = rob2

            newRob = max(take,skip)

            #slide the window forward
            rob1 = rob2 #(as in the next iteration rob2's value is now i-2)
            rob2 = newRob #this becomes i-1 in next iteration
        return rob2

