public class Solution {
    public string DecodeString(string s) {
        Stack<string> stringStack = new();
        Stack<int> repeatStack = new();
        string currString = "";
        int pendingRepeat = 0;

        foreach (char c in s) {
            if (char.IsDigit(c)) {
                pendingRepeat = pendingRepeat * 10 + int.Parse(c.ToString());
            } else if (c == '[') {
                stringStack.Push(currString);
                repeatStack.Push(pendingRepeat);
                currString = "";
                pendingRepeat = 0;
            } else if (c == ']') {
                string outerString = stringStack.Pop();
                int currRepeat = repeatStack.Pop();
                currString = outerString + string.Concat(Enumerable.Repeat(currString, currRepeat));
            } else {
                currString += c;
            }
        }

        return currString;
    }
}