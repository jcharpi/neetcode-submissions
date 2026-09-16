public class Solution {
    public int[][] Merge(int[][] intervals) {
        Array.Sort(intervals, (a, b) => a[0].CompareTo(b[0]));

        var overlapping = new List<int[]>();
        var currInterval = intervals[0];
        for (int i = 1; i < intervals.Length; i++) {
            if (currInterval[1] >= intervals[i][0]) {
                currInterval[1] = Math.Max(intervals[i][1], currInterval[1]);
            } else {
                overlapping.Add(currInterval);
                currInterval = intervals[i];
            }
        }
        overlapping.Add(currInterval);
        return overlapping.ToArray();
    }
}
