public class Solution {
    public bool CheckValidString(string s) {
        int min_open = 0, max_open = 0;
        foreach (char c in s) {
            if (c == '(') {
                min_open++;
                max_open++;
            } else if (c == ')') {
                max_open--;
                min_open--;
            } else {
                min_open--;
                max_open++;
            }

            if (max_open < 0) return false;
            min_open = Math.Max(min_open, 0);
        }
        return min_open == 0;
    }
}
