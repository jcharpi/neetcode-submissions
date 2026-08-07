class Solution {
public:
    string longestPalindrome(string s) {
        string max_substring;

        for (int i = 0; i < s.size(); i++) {
            int l = i, r = i;
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                if (r - l + 1 > ssize(max_substring)) {
                    max_substring = s.substr(l, r - l + 1);
                }
                l--;
                r++;
            }

            l = i, r = i + 1;
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                if (r - l + 1 > ssize(max_substring)) {
                    max_substring = s.substr(l, r - l + 1);
                }
                l--;
                r++;
            }
        }
        return max_substring;
    }
};