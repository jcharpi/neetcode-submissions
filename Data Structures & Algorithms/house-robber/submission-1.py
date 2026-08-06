class Solution:
    def rob(self, nums: List[int]) -> int:
        skip, rob = 0, 0
        for curr in nums:
            skip, rob = max(skip, rob), skip + curr
        return max(skip, rob)