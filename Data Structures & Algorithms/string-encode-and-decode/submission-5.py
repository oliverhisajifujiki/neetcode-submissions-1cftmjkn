class Solution:

    #so we are going to be appending a list of strings to a singular string
    #then taking the single string and split it up properly to recover the list of strings
    #we need a more complex deliminator. a simple deliminator would be confusing in case  the delimin ator actunal ly app,ears in the list of strings 
    #so we use a deliminator that tells us how long each string is so we have these varying deliminators that need to tell us how long each string is
    #so we can sort of think of an int before each string that tells us where to split. 
    #i.e. if the message is "leet" "code" the encoded message is "4leet4code"
    #this works until our string is more than 9 letters or if the string we have starts with a number 
    #i.e. message is "51eggs" the encoding would be "651eggs" confusing on how to decode this.
    #therefore our deliminator will be length of the string thats coming up + $ as a proper deliminator
    #therefore message "leet" "code" would be "4$leet4$code" 

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + str(len(s)) + "$" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        #okay so the idea is we along the string until we see $ say that is in position i
        #take the number between 0 and i say its x
        #then go from i to i+x and that is our first string

        #let i be the index that shows how much of the string we have parsed
        #let j be the index the index that goes from i to our deliminator $
        #therefore now we know the next string is length l = int(s[i:j])
        #and the string is s[j+1: j+1+l] and we append this to decoded
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j = j + 1
            l = int(s[i:j])
            decoded.append(s[j+1: j+1+l])
            i = j + 1 + l
        return decoded


