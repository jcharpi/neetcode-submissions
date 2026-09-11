class Solution {
public:
    int minExtraChar(string s, vector<string>& dictionary) {
        vector<int> dp(ssize(s) + 1, ssize(s) + 1);
        dp[0] = 0;

        for (int i = 1; i < ssize(s) + 1; i++) {
            dp[i] = dp[i - 1] + 1;
            for (const string& word : dictionary) {
                if (s.substr(0, i).ends_with(word)) dp[i] = min(dp[i], dp[i - ssize(word)]);
            }
        }
        return dp.back();
    }
};