public class Solution {
    public bool CanPartitionKSubsets(int[] nums, int k) {       
        int total = nums.Sum();
        int targetSum = (total / k);
        if (total % k != 0) return false;
        
        int[] buckets = new int[k];
        Array.Sort(nums);

        // i is each number being placed
        bool Dfs(int i) {
            if (i < 0) return true;
            if (nums[i] > targetSum) return false;
            
            for (int j = 0; j < k; j++) {
                if (buckets[j] + nums[i] <= targetSum) {
                    buckets[j] += nums[i];
                    if (Dfs(i - 1)) return true;
                    buckets[j] -= nums[i];
                    if (buckets[j] == 0) break;
                }
            }

            return false;
        }

        return Dfs(nums.Length - 1);
    }
}