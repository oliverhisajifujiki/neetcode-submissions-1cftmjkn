class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #okay so we need to init a list of lists
        #this is going to be another dict
        #as we are checking fast members 

        #we will want the frequency of the chars as a key
        #and then the values will be the string itself

        anaDict = {}

        for s in strs:
            key = [0] * 26
            for c in s:
                i = ord(c) - ord("a")
                key[i] += 1
            key = tuple(key)
            if key not in anaDict:
                anaDict[key] = []
            
            anaDict[key].append(s)

        return list(anaDict.values())

