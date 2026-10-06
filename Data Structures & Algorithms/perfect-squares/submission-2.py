class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n + 1] * (n + 1)
        dp[0], dp[1] = 0, 1

        squares = []
        for i in range(1, n + 1):
            if math.sqrt(i) == int(math.sqrt(i)):
                squares.append(i)
            for square in squares:
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[n]