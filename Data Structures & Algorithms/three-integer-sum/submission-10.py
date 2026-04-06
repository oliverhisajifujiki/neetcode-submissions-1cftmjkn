#we want to test each tuple
#getting each tuple and making sure they are unique is not so easy
#o(n^2) wanted we could sort first
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsSorted = sorted(nums)
        n = len(nums)
        res = []

        for i in range(n): #nums[i] becomes new psuedo target, 
            targ = numsSorted[i]
            if i > 0 and numsSorted[i] == numsSorted[i-1]:
                continue
            l = i + 1
            r = n - 1

            while l < r:
                s = targ + numsSorted[l] + numsSorted[r]

                if s == 0: #candidate found 
                    res.append([targ, numsSorted[l], numsSorted[r]])
                    #now we move the pointers
                    #increment l and r
                    l += 1
                    r -= 1
                    while l < r and numsSorted[l] == numsSorted[l-1]: #if equal we just found this candidate no need to go over
                        l += 1
                    
                    while l < r and numsSorted[r] == numsSorted[r+1]:
                        r -= 1
                
                elif s > 0: #this is the case that sum is too large, therefore we want to make it smaller by decrementing l
                    r -= 1
                
                else: 
                    l += 1
        
        return res
