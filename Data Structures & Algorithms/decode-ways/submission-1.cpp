class Solution {
public:
    int numDecodings(string s) {
        unordered_map<int, int> cache = {};
        
        function<int(int i)> count_decodings = [&](int i) -> int {
            if (i == ssize(s)) return 1;
            if (cache.contains(i)) return cache[i];

            int total = 0;
            if (s[i] != '0') total += count_decodings(i + 1);
            if (i + 1 < ssize(s) && 
                (s[i] == '1' || s[i] == '2' && s[i + 1] <= '6')) total += count_decodings(i + 2);
            
            return cache[i] = total;
        };

        return count_decodings(0);
    }
};
