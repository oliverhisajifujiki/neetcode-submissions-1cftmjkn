class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #dp[i] : can suffix s[i:] be broken into valid dictionary words 

        dp = [False] * (len(s) + 1)

        #base case , empty suffix can be segmented 
        dp[len(s)] = True

        #work backwards from the end of the string toward the front
        for i in range(len(s) - 1, -1 , -1):
            #try each word in dictionarry as a possible first word starting at i
            for w in wordDict:
                #if the word fits inside the remaining string
                #and the substring start at i begins with w
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    #then s[i:] is segmentable iff the rest of after w is segmentable
                    if dp[i + len(w)]: #this is the key check, this will tell us if the rest of the substring is segmentable given that we have this candidate w 
                        dp[i] = True
                        break
        
        return dp[0]
