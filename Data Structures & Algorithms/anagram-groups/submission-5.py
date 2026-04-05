class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {} #key: 26 tuple where element i represents the freq of char i in string
        
        for s in strs:
            key = [0]*26
            for c in s:
                i = ord(c) - ord("a")
                key[i] += 1
            key = tuple(key)
            if key not in anaDict:
                anaDict[key] = []
            anaDict[key].append(s) 
        
        return list(anaDict.values())
