class Solution:
    def rob(self, nums: List[int]) -> int:
        #quite similar to stairs number 1 its dp 
            #because the decisions we make on which houses we robbed before
            #defines if we should rob the house n
        #our best answer is going to either robbing house n
        #or not robbing house n
        #if we rob house n we can not rob house n-1
        #therefore the logic flow is either dont rob house n
            #the best robbing strat is the same as if we only had to consider n-1 houses
        #or rob house n 
            #and the best robbing strat is the same as if we only considered n-2 houses + n house
        
        #there for we have two base cases
        #n == 1 nums[0] is the best plan
        #n == 2 max(nums[0], nums[1]) is the best plan

        #everything is built from these two 

        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        return dp[-1] #last robbing plan we calculated
        