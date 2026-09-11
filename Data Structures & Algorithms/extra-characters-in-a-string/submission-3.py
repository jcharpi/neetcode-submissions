class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [len(s) + 1] * (len(s) + 1)
        dp[0] = 0
        for i in range(1, len(s) + 1):
            dp[i] = dp[i - 1] + 1
            for word in dictionary:
                if s.endswith(word, 0, i):
                    dp[i] = min(dp[i], dp[i - len(word)])
        return dp[-1]