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
    public int MinMeetingRooms(List<Interval> intervals) {
        intervals.Sort((a, b) => a.start.CompareTo(b.start));
        var minHeap = new PriorityQueue<Interval, int>();
        foreach (var interval in intervals) {
            if (minHeap.Count > 0 && minHeap.Peek().end <= interval.start) {
                minHeap.Dequeue();
            }

            minHeap.Enqueue(interval, interval.end);
        }

        return minHeap.Count;
    }
}
