class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n 
        #to understand this one i think is easiest to root this in an example
        #nums = [2,3,4,5] the naive calc is
        #ind 0 : 3*4*5
        #ind 1 : 2*4*5 
        #ind 2 : 2*3*5
        #ind 3 : 2*3*4
        #we are doing things multiple times, for e.g 4*5 is appears multiple times 
        #this idea of running products allows us to compute for example 2*3 once and then build off of it for the others that need it 

        #so for this particular problem we use to running products
        #a running product is simply take all numbers before and multiply them
        #therefore we first do res = [1,1,1,1] and then do a running product
        #and keep in mind this leftProduct which is the running product starting from the left
        #leftProduct stores the multiplication we have done
        # so e.g i = 0
        # there is nothing in nums to the left of index 0 so res[0] = 1
        # update leftProduct *= nums[0] = 2
        # i = 1 , everything to the left of index 1 in nums is just 2
        # result[1] = 2 // then update leftProduct *= 3 = 6
        # i = 2 , everything to the left is 3 and then 2 = 6
        # result[2] = 6 // update leftProduct *= 4 = 24
        # i = 3, everything to the left is 4*3*2 = 24
        # result[3] = 24 // update leftProduct *= 5 = 120
        # the key thing here is that at each step we stored the leftProduct so we dont actually have to do any calculation for updating result[i] its already there
        n = len(nums)
        res = [1]*n
        
        #running product on the left side
        leftProd = 1
        for i in range(n):
            res[i] = res[i] * leftProd
            leftProd = leftProd * nums[i]
        
        #running product on the right side
        rightProd = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * rightProd
            rightProd = rightProd * nums[i]
        
        return res



        