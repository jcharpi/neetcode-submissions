class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def count_decodings(i):
            if i == len(s):
                return 1
            
            if i in memo:
                return memo[i]

            total = 0
            if s[i] != "0":
                total += count_decodings(i + 1)
            
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                total += count_decodings(i + 2)
            
            memo[i] = total
            return total
        return count_decodings(0)