class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, seen = 0, set()
        max_length = 0
        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            max_length = max(max_length, len(seen))
        return max_length