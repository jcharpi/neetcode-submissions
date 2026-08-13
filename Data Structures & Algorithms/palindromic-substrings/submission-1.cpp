class Solution {
public:
    int countSubstrings(string s) {
        int out = 0;
        auto expand = [&](int l, int r) {
            while (l >= 0 && r < static_cast<int>(s.size()) && s[l] == s[r]) {
                l--;
                r++;
                out++;
            }
        };

        for (int i = 0; i < static_cast<int>(s.size()); i++) {
            expand(i, i);
            expand(i, i + 1);
        }
        return out;

    }
};
