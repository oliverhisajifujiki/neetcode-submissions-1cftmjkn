class MedianFinder:
    #priority queue DS where next item with highest or lowest priority
        #usually highest or lowest first
    
    #heap is the efficient implementation of a priority queue
    #heaps are not fully sorted, but guarantees the top element is say smallest
        #getting min fast
        #inserting fast
        #removing min fast

    #given we have a data stream, we are maintaing the exact middle whlie numers are arriving
    #easiest way to do this is simply a sorted list and insert into a sorted list
        #this is quite expensive though

    #so the idea is to split the data into two halves 
        #max heap for the smaller half
        #min heap for the larger half 

    def __init__(self):
        #small stores lower half of the numbers
        #pythons implementation of heap is a min heap
            #so we store the negatives and this gives us a psuedo max heap
        self.small = []

        #large stores upper half of the numbers
        #this will be a min heap
        self.large =[]

        #its important to realize now that adding can be easily
            #even though there seems to be a lot of sorting going on
            #once we have the small and large defined adding a single element is easy
            #given x we arbitrarily put the new int in small
            #we check if the top of small[0] > large[0] then we move it over
            #after we check if the sizes are at most 1 off
        

    def addNum(self, num: int) -> None:
        #1) arb push into small
        heapq.heappush(self.small, -num) #-num as thats how we are storing "max" heap

        #2) check if the heaps still adhere to the ordering rule
            #small holds bottom half of numbers large holds top half of numbers
        #note because of the structure of the heaps and because we have only 
            #added 1 element we only have to check to tops of them
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small) #move top of small
            heapq.heappush(self.large, val) #put it into large

            #note it must be sorted as we want now 
        #3) next thing to check is that we are still splitting the numbers evenly
            #the heaps should differ by at most 1

        sizeS = len(self.small)
        sizeL = len(self.large)    
        if sizeL > sizeS + 1: #move top of L into S
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        elif sizeS > sizeL + 1: #elif works as if we enter top if we never need to consider here
            #move top of S into L
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

    def findMedian(self) -> float:
        #whichever heap is largest it's top ele will be median
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.small) < len(self.large):
            return self.large[0]
        
        #if here len are equal, the median is between the two
        return (-self.small[0] + self.large[0]) / 2
        
        


