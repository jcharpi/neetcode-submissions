class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        
        dp = [2, 3]
        for i in range(4, n + 1):
            dp = [dp[1], dp[0] + dp[1]]
        
        return dp[1]
