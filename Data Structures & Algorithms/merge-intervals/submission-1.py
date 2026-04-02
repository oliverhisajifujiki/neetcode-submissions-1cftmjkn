class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #the naive approach would be n^2 for each interval check if it intervals with anything else
        #i dont think there is any other way except sorting first
        #this would bring us to logn*n territory as we know we now only hve to look at 
        #intervals that are consecutive 
        #lets sort on start_i (interval[i] = [start_i,end_i]) 

        res = []
        intervals.sort(key= lambda x: x[0]) #for each list in interval sort on the first element

        curStart, curEnd = intervals[0]

        #go through intervals to see if there are overlaps
        for start, end in intervals[1:]:
            if start <= curEnd: #only need to look at end because we sorted on the start number
                curEnd = max(curEnd, end) 
            
            else:
                #no overlap
                res.append([curStart, curEnd])

                curStart, curEnd = start, end
            
        #after the loop we still need to append the last 
        res.append([curStart, curEnd])

        return res