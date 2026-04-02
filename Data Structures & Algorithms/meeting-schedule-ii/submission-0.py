"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: #empty intervals
            return 0

        intervals.sort(key=lambda x: x.start)

        rooms = [] #min heap of end times 

        for i in range(len(intervals)):
            start = intervals[i].start
            end = intervals[i].end


            #this if is just used to make sure heap is properly counting 
            #how many meetings rooms we use
            #in particular if we need to pop anything
            #also because we are just counting we dont need 
            #details of like how long a meeting room is occupied for 
            #we only need to pop 1 not all empty ones 
            if rooms and rooms[0] <= start:
                #if rooms makes sure its nonempty
                heapq.heappop(rooms)
            
            #now heappush when this meeting will end
            heapq.heappush(rooms,end)

        return len(rooms) #in this implementation we are only removing a room when we look to use it, therefore we always keep the max of how many rooms we've needed


