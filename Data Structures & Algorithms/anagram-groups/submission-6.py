class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we will need a key for each kind of anagram, 
        #a suitable key is a freq array of length 26
            #where element i represents the freq of letter i (where a = 0 and z = 26)

        anaDict = {}

        for s in strs:
            key = [0]*26
            for c in s:
                index = ord(c) - ord("a")
                key[index] += 1
            key = tuple(key)
            if key not in anaDict:
                anaDict[key] = []
            anaDict[key].append(s)
        
        print(anaDict.values())
        return list(anaDict.values())
