class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we need a way of identifying via a key if a string is a part of an anagram
        #think of it in keys because we want to check membership kind of often 

        #therefore lets have an anagram dictionary
            #such that they key is a list of letter and its freq
        
        anaDict = {} #this will have key
                        #a list of size 26, where element i represents 
                        #the freq of letter i (where this index represents where it is in the alphabet)
                        #i.e. a = 0 , z = 26
                    
                    #the value will be s in strs such that it has key freq of letters 
        
        for s in strs:
            key = [0] * 26
            for c in s:
                index = ord(c) - ord("a")
                key[index] += 1
            key = tuple(key)
            if key not in anaDict:
                anaDict[key] = []
            anaDict[key].append(s)
        
        print(anaDict.values())
        return list(anaDict.values())




