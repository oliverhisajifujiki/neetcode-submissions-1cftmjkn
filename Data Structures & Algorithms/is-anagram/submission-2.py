class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #another hash problem
        #count how many of each char is in string s
        #count how many of each char is in string t
        #the key will be the letter 
        #the value will be the frequency
        #if counts match they are anagrams 
        
        #one thing to do first is if the len of each of the strings are different immediately we can return false
        if len(s) != len(t):
            return False

        sDic = {}
        tDic = {}
        #build the dictionaries
        for i in range(len(s)): #at this point they should both be equal length so WLOG caneither do s or t in len
            c = s[i]
            if c not in sDic:
                sDic[c] = 1 #init the freq count
            else:
                sDic[c] = sDic[c] + 1 #else we can simply iterate
            c = t[i] #now look through t
            if c not in tDic:
                tDic[c] = 1
            else:
                tDic[c] = tDic[c] + 1
        
        return sDic == tDic
            
            

