class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, nums = 0, set()
        max_length = 0
        for r, char in enumerate(s):
            while char in nums:
                nums.remove(s[l])
                l += 1
            nums.add(char)
            max_length = max(max_length, len(nums))
            print(nums, max_length)
        return max_length