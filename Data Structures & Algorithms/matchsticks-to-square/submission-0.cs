public class Solution {
    public bool Makesquare(int[] matchsticks) {
        int totalLength = matchsticks.Sum();
        if (totalLength % 4 != 0) return false;
        
        int sideLength = totalLength / 4;
        int[] sides = new int[4];

        bool Dfs(int i) {
            // haven't failed through all considerations so return true
            if (i == matchsticks.Length) return true;

            for (int side = 0; side < 4; side++) {
                if (sides[side] + matchsticks[i] <= sideLength) {
                    sides[side] += matchsticks[i];
                    if (Dfs(i + 1)) return true;
                    sides[side] -= matchsticks[i];
                }
            }

            return false;
        }

        return Dfs(0);
    }
}