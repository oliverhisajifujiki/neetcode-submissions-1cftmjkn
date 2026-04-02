class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #we sort of just have to find where to put this new interval
        #as the inputted array is alr sorted
        #we can look at each i in intervals
        #and there are three cases for intervals[i]
            #1) newInterval > intervals[i]
            #2) newInterval < intervals[i]
            #3) newInterval overlaps with intervals[i]
        
        #in the first two cases nothing special needs to happen we just insert 

        res = []
        newStart, newEnd = newInterval
        i = 0
        for start, end in intervals:
            #case 1
                #current interval is completely before new interval
            
                #no overlap so no need to alter any interval 
                if end < newStart:
                    res.append([start,end]) 
                    i += 1
                
            #case 2
                #current interval is completely after new interval
            
                #no overlap so no need to alter just put the new interval in res
                elif start > newEnd:
                    res.append([newStart, newEnd])
                    #as we have inserted the new interval we are done 
                    res.extend(intervals[i:])
                    return res

            #case 3 
                else: 
                    newStart = min(newStart, start)
                    newEnd = max(newEnd, end)
                    #note that we can't just append here as this new 
                    #enlargened interval can still intersect with other intervals
                    #so we have to check the previous intervals (think of if the interval we are adding [a,b] such that a and b will be the new min and max of the set)
                    i += 1
        res.append([newStart,newEnd])     
        return res #if we haven't inserted anywhere within the loop it belongs at the end!

            
