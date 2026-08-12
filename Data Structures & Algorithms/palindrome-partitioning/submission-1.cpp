class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> out;
        vector<string> curr;

        function<bool(int l, int r)> is_palindrome = [&](int l, int r) -> bool {
            while (l < r) {
                if (s[l] != s[r]) return false;
                l++;
                r--;
            }
            return true;
        };

        function<void(int i)> dfs = [&](int i) -> void {
            if (i == ssize(s)) {
                out.push_back(curr);
                return;
            }

            for (int j = i; j < ssize(s); j++) {
                if (is_palindrome(i, j)) {
                    curr.push_back(s.substr(i, j - i + 1));
                    dfs(j + 1);
                    curr.pop_back();
                }
            }
        };

        dfs(0);
        return out;
    }
};
    