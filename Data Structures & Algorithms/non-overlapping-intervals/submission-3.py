class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval : interval[1])

        latest_end, out = intervals[0][1], 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < latest_end:
                out += 1
            else:
                latest_end = intervals[i][1]
        return out