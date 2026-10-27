public class Solution {
    public bool CheckPossibility(int[] nums) {
        bool hasChanged = false;

        for (int i = 1; i < nums.Length; i++) {
            if (nums[i] >= nums[i - 1]) continue;

            if (hasChanged) return false;
            hasChanged = true;
            
            // i - 2 decides if nums[i - 1] can safely drop to nums[i]
            // Fix nums in place so later checks see it
            if (i > 1 && nums[i - 2] > nums[i]) nums[i] = nums[i - 1];
            else nums[i - 1] = nums[i];
        }
        return true;
    }
}