class Solution {
public:
    string longestPalindrome(string s) {
        string longest;
        for (int i = 0; i < s.size(); i++) {
            for (const string& candidate : { expand(i, i, s), expand(i, i + 1, s) }) {
                if (candidate.size() > longest.size()) longest = candidate;
            }
        }
        return longest;
    }

private:
    string expand(int l, int r, const string& s) {
        while (l >= 0 && r < s.size() && s[l] == s[r]) {
            l--;
            r++;
        }
        l++;
        r--;

        return s.substr(l, r - l + 1);
    }
};