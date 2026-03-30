class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we have to go through each num in this list. and then see if there exists another number in the list that adding to it would give us target
        #because of this i feel like hashing is the solution here again for some sort of fast counting / we will be looking up values 
        nDict = {} #this dictionary will store perhaps the key being the number in the list and the value will be the index because we need that 

        i = 0 #keep track of index
        for x in nums: #the problem i had before was i didn't do a first pass through of checking if target - x is seen and so therefore i was overwriting certain numbers example nums = [5,5] target = 10 wanted [0,1] but i outputted [1,1]
            need = target - x
            if need in nDict:
                return[nDict[need], i]
            
            nDict[x] = i
            i = i + 1

