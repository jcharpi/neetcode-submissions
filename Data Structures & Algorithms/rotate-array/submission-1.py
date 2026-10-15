class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        out, k = [0] * len(nums), k % len(nums)
        for i, num in enumerate(nums):
            out[(i + k) % len(nums)] = num
        nums[:] = out