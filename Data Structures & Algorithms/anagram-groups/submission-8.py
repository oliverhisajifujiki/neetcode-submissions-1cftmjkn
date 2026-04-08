class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #for each string we will construct a "key" 
        #this key will be a 26 length array 
        #where the ith element represents the frequency of the ith element of the alphabet
        res = {}

        for s in strs:
            key = [0]*26
            for c in s:
                index = ord(c) - ord("a")
                key[index] += 1
            key = tuple(key)

            if key not in res:
                res[key] = []
            res[key].append(s)
        
        return list(res.values())
            
