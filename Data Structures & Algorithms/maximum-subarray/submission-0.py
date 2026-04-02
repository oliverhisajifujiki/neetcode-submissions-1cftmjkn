class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0] #safe to do 
        curSum = 0 #counter
        
        for n in nums: #go through all the numbers
            if curSum < 0: #if counter ever goes negative just restart
                    curSum = 0 
            
            curSum += n #greedily just add n no matter what
            best = max(best, curSum) #take 

        return best