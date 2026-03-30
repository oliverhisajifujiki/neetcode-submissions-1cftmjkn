class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #a hash is the best way to do these as brute force
        #will have to be nested for loops and be O(n^2)
        #we can sort first, but thats going to be O(nlogn)
        #but then we only have to compare the side by side elements
        #so only 1 forloop needed 
        #hash will be O(n) (implementing the hash) and then checking for dupes will be O(1)

        #use a set as this will be lightest weight thing to implement
        seen = set()
        #go through each number in nums and first check if is in seen yet (would return true) and then add it to seen if not
        for num in nums:
            if num in seen:
                return True

            seen.add(num)
        return False