class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        max_profit = 0

        while sell < len(prices):
            # case 1: profitable
            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, prices[sell] - prices[buy])                
            # case 2: not profitable
            else: 
                buy = sell
            sell += 1
        return max_profit