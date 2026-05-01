class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2 3 4 5       10      20
        # if has left neighbor, length = 0, 
        # while num + length in set, curr++, max = max(curr, longest)
        # return nums

        nums_set = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums_set:
                length, current = 0, 0
                while num+length in nums_set:
                    current += 1
                    longest = max(current, longest)
                    length += 1
        return longest