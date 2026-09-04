public class Solution {
    public List<int> FindClosestElements(int[] arr, int k, int x) {
        bool IsCloser(int a, int b) {
            return Math.Abs(a - x) < Math.Abs(b - x) || 
                (Math.Abs(a - x) == Math.Abs(b - x) && a < b);
        }

        Queue<int> window = new Queue<int>(k);
        int left = 0;

        for (int right = 0; right < arr.Length; right++) {
            if (window.Count < k) window.Enqueue(arr[right]);
            else if (IsCloser(arr[right], arr[left])) {
                window.Dequeue();
                window.Enqueue(arr[right]);
                left++;
            }
        }

        return window.ToList();
    }
}