class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max_seq = 0

        for num in my_set:
            if num - 1 not in my_set:
                length = 1
                while num + length in my_set:
                    length += 1
                max_seq = max(max_seq, length)
            print(max_seq)

        return max_seq