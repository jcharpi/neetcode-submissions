class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0
        for num in num_set:
            if num - 1 in num_set:
                continue

            length = 0
            while num + length in num_set:
                length += 1
                max_seq = max(max_seq, length)
        return max_seq