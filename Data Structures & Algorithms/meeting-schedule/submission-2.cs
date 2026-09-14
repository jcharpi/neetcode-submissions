/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

public class Solution {
    public bool CanAttendMeetings(List<Interval> intervals) {
        intervals.Sort((a, b) => a.start.CompareTo(b.start));
        int latest_time = 0;
        foreach (Interval interval in intervals) {
            if (interval.start < latest_time) {
                return false;
            }
            latest_time = interval.end;
        }
        return true;
    }
}
