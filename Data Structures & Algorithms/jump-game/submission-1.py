class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0

        for i, num in enumerate(nums):
            if max_reachable < i:
                return False
            max_reachable = max(max_reachable, i + num)
        return max_reachable >= len(nums) - 1