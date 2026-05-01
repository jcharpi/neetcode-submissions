class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in nums:
            # check start of seq?
            if (num - 1) not in num_set:
                # yes: does num + 1 exist?
                length = 0
                while (num + length) in num_set:
                    length += 1
                # update longest
                longest = max(longest, length)
        return longest
                    