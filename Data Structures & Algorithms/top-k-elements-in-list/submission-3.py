class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bucket = [[] for _ in range(n + 1)]
        #bucket sort, the ith list contains a number (say x), and that indicates that
            #x has appeared in nums i times
            #we then go backwards in in the list until we see k numbers 
        numsDict = {} #key is number , value is freq
        res = []
        
        for num in nums:
            if num not in numsDict:
                numsDict[num] = 0
            numsDict[num] += 1

        for key, item in numsDict.items():
            bucket[item].append(key)
        
        for i in range(n , 0, -1):
            print(i)
            print(bucket[i])
            for x in bucket[i]:
                res.append(x)
                print(res)
                if len(res) == k:
                    return res
                





