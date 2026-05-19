class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, nums = 0, set()
        max_length = 0
        for r in range(len(s)):
            while s[r] in nums:
                nums.remove(s[l])
                l += 1
            nums.add(s[r])
            max_length = max(max_length, len(nums))
        return max_length