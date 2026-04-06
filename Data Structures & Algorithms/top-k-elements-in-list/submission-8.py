class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #so we want to use a dictionary pass through the numbers
        nDict = {}

        for n in nums:
            if n not in nDict:
                nDict[n] = 0
            nDict[n] += 1

        #now we have each number and its frequency in a dictionary

        #we have to find a smart way to sort this 

        #we bucket sort this

        bucket = [[] for _ in range(len(nums) + 1)] 

        #what bounds do we need for this bucket sort, at max we have freq len(nums) range is not inclusive so + 1
        #bucket[i] will store numbers (say x) such that the frequency of x in nums is i
        for key, val in nDict.items():
            bucket[val].append(key)

        #now we just have to traverse this list backwards , and each number we see we add this to our result and check if we have k results
        res = []


        
        for i in range(len(nums), -1, -1): #again range is non-inclusive so -1 should get us to bucket[0]
            print(i)
            for x in bucket[i]: #note if bucket[i] is just empty appending it wil not hurt us at all
                res.append(x)
                if len(res) == k:
                    return res

        #don't need an outside return here as we are ensured that there are at least k distinct nums



