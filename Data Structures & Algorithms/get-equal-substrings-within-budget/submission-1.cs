public class Solution {
    public int EqualSubstring(string s, string t, int maxCost) {
        int maxIntervals = 0;

        int currCost = 0, l = 0;
        for (int r = 0; r < s.Length; r++) {
            int currSwapCost = Math.Abs(s[r] - t[r]);
            currCost += currSwapCost;
            while (currCost > maxCost) {
                currCost -= Math.Abs(s[l] - t[l]);
                l++;
            }

            maxIntervals = Math.Max(maxIntervals, r - l + 1);
        }

        return maxIntervals;
    }
}
