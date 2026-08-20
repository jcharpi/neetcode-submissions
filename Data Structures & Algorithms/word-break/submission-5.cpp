class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<optional<bool>> cache(ssize(s) + 1);
        cache[0] = true;

        function<bool(int i)> can_break = [&](int i) -> bool {
            if (cache[i].has_value()) return *cache[i];

            string_view prefix(s);
            prefix = prefix.substr(0, i);
            cache[i] = false;
            for (const string word : wordDict) {
                if (prefix.ends_with(word) && can_break(i - ssize(word))) {
                    cache[i] = true;
                    break;
                }
            }
            return *cache[i];
        };

        return can_break(ssize(s));
    }
};
