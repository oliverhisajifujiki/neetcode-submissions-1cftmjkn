class Solution:
    def numDecodings(self, s: str) -> int:
        #very much like 2stairs 
        #we have two choices, either we take the two digits as an encoding of a single char
            #or the two digits encode to two seperate chars
        
        #there are slightly more rules, 
            #single digit is valid if it is not "0"
            #two digist are valid if they between 10 - 26
        
        #just like the 2stairs we store every single decoding that it could be of the n-1 digits
            #then we add on two possibilities to each decoding for n digits
                #either we simply add n'th digit to all possibilities (as long as n != 0)
                #or if the previous number was 1 or 2, and if the digit we are adding are between 0-6
                    #then we could consider the nth and n-1 digit to be encoding of a letter
                    # add this to all possibilities
                
            #there are some key things i realize now though. we can not simply look at the digit in front 
            #we'll also need to make sure that this digit is either
                #interpreted as a single decoding 
                #if it is part of a pair , the number in front of it is not 0, else we would be left with a 0 alone, and this does not decode to anything
            
            #look last 2 characters s[i-2:i]
            #we need 2 checks 
                #1, that s[i-2] is 1 or 2
                #2, that s[i-1] can be anything if s[i-2] is 1
                    #or can be 0 to 6 if s[i-2] is 2
            #example where we distilled too much, what we are really checking 
                #is if s[i-2] and s[i-1] joined is between 10 and 26,
                #this are the valid 2digit interpetations
        
        #if the string starts with 0, no valid decodings
        if not s or s[0] == "0":
            return 0

        #let dp[i] = number ways to decode the first i characters of s

        #dp[0] = 1 (1 way to decode empty prefix)
        #dp[1] = 1 (if first char is valid)
        n = len(s)
        dp = [0] * (n+1)


        dp[0] = 1
        dp[1] = 1 #if we are here we alr passed the first check

        #now build from left to right
        for i in range(2, n+1):
            #one digit option:
            #check that the char is not 0 (or else it has to be part of a two digit decoding)
            #note the index change 
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            

            #two-digit option:
            #if the last two characters s[i-2] and s[i-1] joined are between 10 and 26
            twoDigitCheck = int(s[i-2:i])
            if 10 <= twoDigitCheck <= 26:
                dp[i] += dp[i-2]
            
        #answer = number of ways to decode the whole string
        return dp[n]



