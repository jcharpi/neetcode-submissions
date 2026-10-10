public class Solution {
    public int FindPeakElement(int[] nums) {
        int l = 0, r = nums.Length;

        bool isPeak(int i) {
            if ((i > 0 && nums[i - 1] > nums[i]) || 
                (i < nums.Length - 1 && nums[i + 1] > nums[i])) return false;
            return true;
        }

        // revisit condition
        while (l < r) {
            int mid = (l + r) / 2;
            Console.WriteLine($"{isPeak(mid)}, mid = {mid}, l = {l}, r = {r}");
            if (!isPeak(mid)) {
                // if left is out of array or smaller than right, set left to mid + 1
                if (mid - 1 < 0 || (mid + 1 < nums.Length && nums[mid - 1] < nums[mid + 1])) l = mid + 1;
                else r = mid - 1;
            } else {
                return mid;
            }
        }
        return l;
    }
}