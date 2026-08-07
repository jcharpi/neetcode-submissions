class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            return s[l:r + 1]

        for i in range(len(s)):
            for candidate in [expand(i, i), expand(i, i + 1)]:
                if len(candidate) > len(longest):
                    longest = candidate
        
        return longest

        