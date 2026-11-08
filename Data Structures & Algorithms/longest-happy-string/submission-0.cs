public class Solution {
    public string LongestDiverseString(int a, int b, int c) {
        string result = "";

        bool IsRepeatingChar(char c) {
            return result.Length >= 2 && 
                result[^1] == c &&     
                result[^2] == c;
        }

        PriorityQueue<char, int> maxHeap = new(Comparer<int>.Create((x, y) => y.CompareTo(x)));
        if (a > 0) maxHeap.Enqueue('a', a);
        if (b > 0) maxHeap.Enqueue('b', b);
        if (c > 0) maxHeap.Enqueue('c', c);

        while (maxHeap.TryDequeue(out char ch, out int count)) {
            
            if (IsRepeatingChar(ch)) {
                if (!maxHeap.TryDequeue(out char nextCh, out int nextCount)) break;
                result += nextCh;
                nextCount--;
                if (nextCount > 0) maxHeap.Enqueue(nextCh, nextCount);
            } else {
                result += ch;
                count--;
            }
            if (count > 0) maxHeap.Enqueue(ch, count);
        }

        return result;
    }
}