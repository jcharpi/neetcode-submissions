"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval : interval.start)

        latest_end = 0
        for interval in intervals:
            if interval.start < latest_end:
                return False
            latest_end = interval.end
        return True