public class Solution {
    public int SubsetXORSum(int[] nums) {
        int Dfs(int i, int runningTotal) {
            if (i == nums.Length) {
                return runningTotal;
            }

            return Dfs(i + 1, runningTotal) + Dfs(i + 1, runningTotal ^ nums[i]);
        }

        return Dfs(0, 0);
    }
}