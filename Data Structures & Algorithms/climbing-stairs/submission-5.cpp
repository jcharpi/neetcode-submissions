class Solution {
public:
    int out = 0;
    unordered_map<int, int> cache = {};

    int climbStairs(int n) {
        
        if (n < 3) return n;
        if (cache.contains(n)) return cache[n];

        cache[n] = climbStairs(n - 2) + climbStairs(n - 1);

        return cache[n];
    }
};
