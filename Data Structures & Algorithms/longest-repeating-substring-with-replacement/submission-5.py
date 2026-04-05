class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window obvious here
        #l = 0 again and r = 0 starting but in the for loop 
        #we have a slice dictionary where the key is the char and value is freq of char
        #siceDict = {}
        #we have a longest and maxFreq that we want to keep track of
        #longest is longest window, and maxFreq keeps track of the highest freq letter
        #the point of maxFreq is to check len(s[l:r]) - maxFreq <= k 
            #note len(s[l:r]) easier computed l - r + 1

        #if this is true this slice is still valid 
        #if this window is not valid we must slide the slice (l += 1)
        #before computing the slide though it is efficient to first change the dict
        #sliceDict[s[l]] -= 1 as our window is losing s[l]
        #then l += 1

        l = 0
        maxF = 0
        longest = 0
        sliceDict = {}

        for r in range(len(s)):
            if s[r] not in sliceDict: #update the dictionary
                sliceDict[s[r]] = 0
            sliceDict[s[r]] += 1

            if sliceDict[s[r]] > maxF: #check to see if we have to update maxF
                #as we have only changed the freq of s[r] only need to check that count
                maxF = sliceDict[s[r]]
            
            
            if (r - l + 1) - maxF > k: #not an if because s[r] == s[l+1] is a possibility and then we'd need to increment l again
                sliceDict[s[l]] -= 1
                l += 1

            if (r - l + 1) > longest:
                longest = r - l + 1

        return longest

        