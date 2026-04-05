class Solution:

    def encode(self, strs: List[str]) -> str:
        #encoder has to be number first then a deliminator
        #deliminator can truly be anything
        #as this encoding will work smoothly no matter what we see as long as we have number 
            #which describes how many chars is in the next string 
        
        #e.g leet code is fun -> 4$leet4$code2$is3$fun

        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "$" + s
        
        return encoded

    def decode(self, s: str) -> List[str]:
        #decoding is pretty straight forward, 
            #though you need two indices, 1 for where the last word ended
            #                             2 for where you then see the $
            #we then take the number that we read between 1 and 2 
        
        res = []
        i = 0
        while i < len(s): #the trick here is that we are always going to be started at pointing properly to the beginning of the number for encoding
            j = i
            while s[j] != "$":
                j = j + 1 
            #once we are here i is the correct index for our deliminator $
            #we look at the slice from j to i - 1
            strLen = int(s[i:j])
            #can update j here
            j += 1
            res.append(s[j:j+strLen])

            i = j + strLen
        return res

            


