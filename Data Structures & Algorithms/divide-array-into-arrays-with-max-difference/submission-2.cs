public class Solution {
    public int[][] DivideArray(int[] nums, int k) {
        Array.Sort(nums);
        int groupsNeeded = nums.Length / 3;
        int[][] result = new int[groupsNeeded][];

        for (int i = 0; i < nums.Length; i += 3) {
            if (nums[i + 2] - nums[i] > k) return [];
            result[i / 3] = [nums[i], nums[i + 1], nums[i + 2]];
        }

        return result;
    }
}
