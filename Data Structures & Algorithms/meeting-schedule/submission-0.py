"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #again sorting is clearly the best way or else we'd have to compare to much
        #lets sort on start time
        #check neighbouring meetings
        #if we find an overlap return false

        intervals.sort(key=lambda x: x.end)

        #check each meeting against the one right before it
        for i in range(1, len(intervals)):
            prevStart, prevEnd = intervals[i -1].start , intervals[i-1].end
            curStart, curEnd = intervals[i].start, intervals[i].end

            if curStart < prevEnd:
                return False

        return True