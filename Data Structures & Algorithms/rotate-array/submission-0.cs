public class Solution {
    public void Rotate(int[] nums, int k) {
        // Given
        // k is non negative

        // Goal
        // rotate by k steps

        // Dsa
        // just seems array

        // split into 0:k and k:nums length
        // add latter to former

        k = k % nums.Length;
        int[] left = nums[..(nums.Length - k)], right = nums[(nums.Length - k)..];
        right.Concat(left).ToArray().CopyTo(nums, 0);
    }
}