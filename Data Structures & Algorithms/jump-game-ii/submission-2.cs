public class Solution {
    public int Jump(int[] nums) {
        int l = 0, r = 0, result = 0;

        while (r < nums.Length - 1) {
            int max_reachable_index = 0;
            for (int i = l; i < r + 1; i++) {
                max_reachable_index = Math.Max(max_reachable_index, i + nums[i]);
            }
            l = r + 1;
            r = max_reachable_index;
            result++;
        }
        return result;
    }
}
