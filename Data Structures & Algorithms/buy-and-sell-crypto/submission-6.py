class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, best = 0, 1, 0

        while r < len(prices):
            curr = prices[r] - prices[l]
            best = curr if curr > best else best

            if prices[l] > prices[r]:
                l = r

            print(l, r, best)

            r += 1
        return best

        # []
