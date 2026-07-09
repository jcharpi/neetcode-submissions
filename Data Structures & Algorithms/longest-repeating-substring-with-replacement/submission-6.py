class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = Counter()
        most_freq = 0
        l = 0
        for r, char in enumerate(s):
            window[char] += 1
            most_freq = max(most_freq, window[char])
            if (r - l + 1) - most_freq > k:
                window[s[l]] -= 1
                l += 1
            
        return r - l + 1 if s else 0
