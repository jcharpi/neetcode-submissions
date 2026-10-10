public class Solution {
    public int FindPeakElement(int[] nums) {
        int l = 0, r = nums.Length - 1;

        bool isPeak(int i) {
            if ((i > 0 && nums[i - 1] > nums[i]) || 
                (i < nums.Length - 1 && nums[i + 1] > nums[i])) return false;
            return true;
        }

        while (l < r) {
            int m = (l + r) / 2;
            if (!isPeak(m)) {
                if (nums[m] < nums[m + 1]) l = m + 1;
                else r = m - 1;
            } else {
                return m;
            }
        }
        return l;
    }
}