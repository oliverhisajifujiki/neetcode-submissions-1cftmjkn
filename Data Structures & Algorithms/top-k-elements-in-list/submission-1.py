class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #i remember this as a bucket sort
        #a lil complex i dont know how much gain you would get
        #we could do a dictionary 
        numDict = {}

        for n in nums:
            if n not in numDict:
                numDict[n] = 0
            numDict[n] += 1
        
        #maybe do bucket sort
        n = len(nums)
        bucketSort = [[] for _ in range(n + 1)]
        for key, value in numDict.items():
            #here the key is what we want to append to bucketSort[value]
            bucketSort[value].append(key)
        
        res = []
        n -= 1
        while len(res) < k:
            if bucketSort[n]:
                for i in bucketSort[n]:
                    res.append(i)
            
            n -= 1

            
        
        return res[:k] 


