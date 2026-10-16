class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        today_span = 1
        while self.stack and self.stack[-1][0] <= price:
            day = self.stack.pop()
            today_span += day[1]
        self.stack.append((price, today_span))
        return today_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)