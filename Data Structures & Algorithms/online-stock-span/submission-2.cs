public class StockSpanner {
    private readonly Stack<(int Price, int Span)> stack = new();
    
    public int Next(int price) {
        int todaySpan = 1;
        while (stack.Count > 0 && stack.Peek().Price <= price) {
            var day = stack.Pop();
            todaySpan += day.Span;
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






