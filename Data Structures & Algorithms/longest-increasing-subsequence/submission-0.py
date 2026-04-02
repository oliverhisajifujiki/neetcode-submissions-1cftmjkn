class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i] = length of the longest increasing subsequence that ends exactly at index i
        dp = [1] * len(nums)

        #the idea is position i check to see how many if for any value at j is less than
        #if j is less than we know that dp[i] is at least dp[j] + 1

        for i in range(len(nums)):
            for j in range(i):
                # nums[i] can extend a subsequence ending at j if nums[i] > nums[j]
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1) #this is key as we dont need to save all subsequences
                    #we just consider what is the largest subsequence we can build
                    #we have saved the best subsequence into dp[j] 
                    #so we check which dp[j] + 1 is the highest and save it iteratively

        
        #the overall longest increasing subsequence can end anywhere so we check for max
        return max(dp)