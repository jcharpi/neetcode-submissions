public class StockSpanner {
    private Stack<(int price, int span)> stack;

    public StockSpanner() {
        stack = new();
    }
    
    public int Next(int price) {
        int todaySpan = 1;
        while (stack.Count > 0 && stack.Peek().price <= price) {
            var day = stack.Pop();
            todaySpan += day.span;
        }
        stack.Push((price, todaySpan));
        return todaySpan;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.Next(price);
 */






