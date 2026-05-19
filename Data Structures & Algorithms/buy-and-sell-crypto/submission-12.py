class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_seen = float('inf')

        for num in prices:
            max_profit = max(max_profit, num - min_seen)
            min_seen = min(min_seen, num)

        return max_profit