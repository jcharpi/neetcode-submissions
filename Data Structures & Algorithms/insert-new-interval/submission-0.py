class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        for i, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                out.append(interval)
            elif newInterval[1] < interval[0]:
                out.append(newInterval)
                return out + intervals[i:]
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        out.append(newInterval)
        return out