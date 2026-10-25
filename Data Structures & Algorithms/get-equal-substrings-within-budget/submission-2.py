class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_interval, l = 0, 0

        def getCost(a, b):
            return abs(ord(a) - ord(b))

        curr_cost = 0
        for r in range(len(s)):
            curr_cost += getCost(s[r], t[r])
            while curr_cost > maxCost:
                curr_cost -= getCost(s[l], t[l])
                l += 1
            max_interval = max(max_interval, r - l + 1)
        return max_interval

