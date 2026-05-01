class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = curr_ones = 0
        for num in nums:
            if num == 0:
                max_ones = max(max_ones, curr_ones)
                curr_ones = 0
            else:
                curr_ones += 1
        return max(max_ones, curr_ones)