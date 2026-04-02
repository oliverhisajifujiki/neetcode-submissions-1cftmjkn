class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort the interval by end time 
        #makes greedy easy as the earlier we end the more space we have for another interval
        intervals.sort(key=lambda x: x[1])

        #count how many intervals we keep 
        kept = 1 #at min we will keep one (guaranteed to be non empty input)

        #this first interval we always keep 
            #as we have sorted for the end time we know that the lowest end time will give us the most space for other intervals
            #so we will always keep intervals[0] 
        
        # end of the interval we are keeping will be prevEnd
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            #here we just greedily take anything that fits! 
            if start >= prevEnd:
                kept += 1
                prevEnd = end

        
        return len(intervals) - kept


