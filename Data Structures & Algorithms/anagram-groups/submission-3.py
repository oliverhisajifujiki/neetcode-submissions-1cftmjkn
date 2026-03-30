class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #okay so we know how to check for anagrams between two string here now the difference comes from the fact that we will sort of have to check all pairwise so im thinking we can as we are building the dicts for each string we then check and either put it in the list i think this would be nlogn though because we would get at worst a nested for loop where the outside loop runs n times and the inside loop runs i times where i is the current index the outer loop is O(n^2)
        #clearly not the correct way, now we will have to use some sort of key value where the key is some unique key for any string and then the value would be a list of the strings that have the same key
        #i would then return list(dict.values())

        #the hard part about this is the key
        #for each anagram one key could be the sorted(s) but because this returns a list we'd join the list "".join(sorted(s)) could be a clean 
        #another key could be a tuple with 26 elements where the element i represents the freq. of a char . where i = ord(char)

        #the sorted method would sort in O(klogk) where k is the length of the string
        #the big tuple would be O(k) so lets do the big tuple way
        anaDict = {}

        for s in strs:
            #have to create the key first
            count = [0]*26
            for c in s:
                ele = ord(c) - ord('a') #this finds out which element we have to update the frequency of 
                count[ele] = count[ele] + 1
            
            #now the key has to be a tuple instead of a list
            key = tuple(count)

            #now we have the key we simply either create a key value pair, or we append it if it already exists
            if key not in anaDict:
                anaDict[key] = []
            anaDict[key].append(s)
            
        return list(anaDict.values())

