public class Solution {
    public int MinExtraChar(string s, string[] dictionary) {
        List<int> dp = new List<int>();
        for (int i = 0; i < s.Length + 1; i++) dp.Add(s.Length + 1);
        dp[0] = 0;

        for (int i = 1; i < s.Length + 1; i++) {
            dp[i] = dp[i - 1] + 1;
            foreach (string word in dictionary) {
                if (s.Substring(0, i).EndsWith(word)) dp[i] = Math.Min(dp[i], dp[i - word.Length]);
            }
        }
        return dp[^1];
    }
}