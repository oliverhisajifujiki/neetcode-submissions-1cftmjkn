class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #again as the are adding up freequency of something up from a list hash makes the most sense
        #key: integer value: frequency
        #and i think we would just get the 2 highest values from the dictionary, im not sure how to do that though

        #the difficult thing about this problem would be a nice way to sort to get the k highest values
        #bucket sort will be nice here creating the buckets is always a weird one 
        #the buckets are needed because there can be multiple numbers that have the same frequency. if it were the case that it was guaranteed that each integer appeared a unique amount of times instead of the buckets we could just do freq = [0]*(len(nums)+1)

        numDict = {}

        for x in nums: #fill in dictionary from nums
            if x not in numDict:
                numDict[x] = 0
            numDict[x] = numDict[x] + 1

        bucket = [] #create the buckets

        for _ in range(len(nums) + 1):
            bucket.append([])
        
        #now we have to fill the buckets so bucket[value] = key is how we want to populate it
        for key, val in numDict.items():
            bucket[val].append(key)
        
        res = [] #now we have to go backwards in the buckets and take the first k integers we see

        for i in range(len(bucket) - 1, 0, -1): #range(start,end,step)
            for x in bucket[i]:
                res.append(x)
                if len(res) == k:
                    return res
                    


        

