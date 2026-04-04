class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window if we where for a particular slice s[l:r]
        #we keep track of which char has highest freq
            #we check if (size of the slice) - (highest freq char) > k
                        #(l - r + 1) - maxFreq > k
                #if so s[l:r] slice is not valid
                #if slice not valid shift l over one (update freq dictionary)
                    #sort of until (l-r+1) - maxFreq <= k
                
                #and then we just keep track of largest (l-r+1) we get
        
        #highest freq, can be calculated via a dictionary whose 
        #key is the char and value is the frequency of the char in slice

        l = 0
        longest = 0
        maxFreq = 0
        sliceDict = {}

        for r in range(len(s)):
            c = s[r]
            if c not in sliceDict:
                sliceDict[c] = 0
            
            sliceDict[c] += 1

            maxFreq = max(sliceDict[c], maxFreq)

            while (r - l + 1) - maxFreq > k: #because of the calculation done we are never worreid about l > r or 
                #not a valid slice
                sliceDict[s[l]] -= 1 
                l += 1
                #important there as maxFreq can be stale
                    #the reason we do not care about the staleness of maxFreq 
                    #is because we are only incrementing our window by 1 in this loop (wrt r)
                    #and we never will shrink too far becaues maxFreq is too high
            
            longest = max(longest, r - l + 1)
        
        return longest
            



