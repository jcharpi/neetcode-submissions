class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # iterate through
        # if num-1 not in nums
        # 2 3 4 5            10            20
        # 20 => 20: 1
        # 10 => 10: 1
        # 5 ? 4 in nums, so continue; curr += 1
        # 4 ? 3 in nums so continue; curr += 1
        # 3 ? 2 in nums so continue; curr += 1
        # 2 => 4

        # want fast look ups so make nums into set; also gets rid of duplicates
        numSet = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                
                longest = max(longest, length)
        return longest
            
            