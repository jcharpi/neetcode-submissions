public class Solution {
    public int NumSquares(int n) {
        int[] dp = new int[n + 1];
        Array.Fill(dp, n + 1, 1, n);

        List<int> squares = [];
        for (int i = 1; i < n + 1; i++) {
            if ((int)Math.Sqrt(i) == Math.Sqrt(i)) squares.Add(i);
            foreach (int square in squares) {
                dp[i] = Math.Min(dp[i], dp[i - square] + 1);
            }
        }

        return dp[n];
    }
}
