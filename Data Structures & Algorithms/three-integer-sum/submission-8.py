class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #dealing with duplicates is a pain
        #sorting first also allows us to employ 2 pointer strategy
        s = sorted(nums)
        res = []
        n = len(nums)

        for i in range(n):
            targ = s[i] #psuedo target to find n + m = numSort[i]
            if i > 0 and targ == s[i-1]: #check if we just looked at the same number in the prev 
                continue
            l = i + 1
            r = n - 1
            while l < r:
                a = targ + s[l] + s[r]
                if a == 0:
                    #found a tiplet that works
                    res.append([targ, s[l], s[r]])
                    l += 1
                    r -= 1
                    while l < r and s[l] == s[l - 1]:
                        l += 1 #just so we dont look for the same triplet
                    
                    while l < r and s[r] == s[r + 1]:
                        r -= 1
                    
                elif a > 0: #the sum is too big as the list is sorted we know we can shift smartly
                    #if we are too big then shift the right pointer 
                    r -= 1
                    #check if s[r] and s[r+1] are equiv
                    while l < r and s[r] == s[r+1]:
                        r -= 1
                
                else: #the sum is too small 
                    l += 1
                    while l < r and s[l] == s[l-1]:
                        l+=1
        return res        

            
            