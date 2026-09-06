public class Solution {
    public int FindJudge(int n, int[][] trust) {
        int[] netTrust = new int[n + 1];

        foreach (int[] edge in trust) {
            netTrust[edge[0]]--;
            netTrust[edge[1]]++;
        }

        for (int i = 0; i < n + 1; i++) {
            if (netTrust[i] == n - 1) return i;
        }

        return -1;
    }
}