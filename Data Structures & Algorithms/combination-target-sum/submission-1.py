class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #classic for backtracking becaus we want all combinations
            #if we want all combinations / permutations / valid configs; backtracking is good
                #yes/no through many possibilities
        #mental picture make a choice -> go deeper -> undo choice -> make another choice
        
        #for this one we will be thinking about recursively calling a backtrack function
            #backtrack(i, cur, total)
                #i is the current index 
                #cur is the numbers we have chosen to add to our sum
                #total is the sum we are at now 

            #we start by calling backtrack(0, [], 0)
            #if total == target then we add the cur list to res
                #append it a copy of cur 
                    #why a copy? 
            
            # we can do some tricks that allows us not to have to recalculate sums 
        res = []

        def backtrack(i, cur, total):
            #check if total is the target if so save cur
            if total == target:
                res.append(cur.copy()) #its a copy because we will pop some items from cur and reuse the calculations
                return
            
            if i >= len(nums) or total > target: #our base cases technically
                return
            
            #if we are here there is space to add to total
            #now add nums[i] and recurse 
            cur.append(nums[i])
            backtrack(i, cur, total+nums[i])

            #if we are here we returned from recursion either cause we hit target or went over
            #either way undo choice and pick a different path

            cur.pop()

            backtrack(i+1, cur, total) #i+1 is diff path
        
        backtrack(0, [], 0)
        return res



        