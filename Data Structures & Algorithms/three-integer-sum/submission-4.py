class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #if we keep it random , i simply do not know how we would get all triples
        #therefore i think we need to sort 
        nSorted = sorted(nums)
        #as we are looking for a+b+c = 0 we can enable two pointers by solving 
        #a + b = -c , so target becomes for example the first element and we do pointer solve on the rest
        #we are returning a list of lists so initialize here
        res = []
        n = len(nums) 

        #go through the list and check if nSorted[i] 
        
        for i in range(n):
            #uniqueness enforcer because sorted only need to look at prev is the same
            targ = nSorted[i] #psuedo target a + b = -c
            if i > 0 and targ == nSorted[i-1]:
                continue 
            l = i + 1
            r = n - 1
            
            while l < r:
                s = targ + nSorted[l] + nSorted[r]
                if s == 0:
                    res.append([targ, nSorted[l], nSorted[r]]) 
                    #we also have to move l AND r here, as only moving one would give non-unique tuples
                    l += 1
                    r -= 1
                    #we need another uniqueness test here is l gets updated to the same number we'd return non unique tuples
                    while l < r and nSorted[l] == nSorted[l-1]:
                        l += 1
                    while l < r and nSorted[r] == nSorted[r+1]:
                        r -= 1

                elif s > 0: #similar to sum target as before
                    r -= 1
                    #if we are duplicated we alr know here that this sume wont work
                    while l < r and nSorted[r] == nSorted[r+1]:
                        r -= 1
                else:
                    l += 1
                    while l < r and nSorted[l] == nSorted[l-1]:
                        l += 1            
        return res
