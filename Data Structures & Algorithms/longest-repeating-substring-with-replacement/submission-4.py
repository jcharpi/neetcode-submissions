class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, counts = 0, {}
        most_freq = 0
        for r, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            most_freq = max(most_freq, counts[char])
            while (r - l + 1) - most_freq > k:
                counts[s[l]] -= 1
                l += 1
        return r - l + 1 if counts else 0
