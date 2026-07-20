class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> window;
        int left = 0;
        int max_substring = 0;
        for (char c : s) {
            while (window.contains(c)) {
                window.erase(s[left]);
                left++;
            }
            window.insert(c);
            max_substring = max(max_substring, (int)window.size());
        }
        return max_substring;
    }
};
