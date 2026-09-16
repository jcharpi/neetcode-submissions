class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval : interval[0])
        
        out, curr_interval = [], intervals[0]
        for i in range(1, len(intervals)):
            if curr_interval[1] >= intervals[i][0]:
                curr_interval[1] = max(intervals[i][1], curr_interval[1])
            else:
                out.append(curr_interval)
                curr_interval = intervals[i]
        out.append(curr_interval)
        return out