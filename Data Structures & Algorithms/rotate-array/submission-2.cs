public class Solution {
    public void Rotate(int[] nums, int k) {
        int n = nums.Length;
        k = k % n;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[(i + k) % n] = nums[i];
        }
        Array.Copy(result, nums, n);
    }
}