class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nDict = {}
        for n in nums:
            if n not in nDict:
                nDict[n] = 0
            nDict[n] += 1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, val in nDict.items():
            bucket[val].append(key)
        
        res = [] #a list that will be length k, that we will return! 

        for i in range(len(nums), -1 ,-1):
            #print(bucket[i])
            for x in bucket[i]:
                res.append(x)
                if len(res) == k:
                    return res
        
        return res