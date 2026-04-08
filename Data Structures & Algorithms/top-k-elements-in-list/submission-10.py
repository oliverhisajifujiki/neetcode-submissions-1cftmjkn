class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nDict = {}
        for n in nums:
            if n not in nDict:
                nDict[n] = 0
            
            nDict[n] += 1
        
        n = len(nums)
        bucket = [[] for _ in range(n + 1)] 
        #want to make sure we have at least n lists in bucket
            #range is non-inclusive for end point
        
        for key, val in nDict.items():
            bucket[val].append(key)
        
        res = []
        for i in range(n, -1 , -1):
            for x in bucket[i]:
                res.append(x)
                if k == len(res):
                    return res
        
        return res
        