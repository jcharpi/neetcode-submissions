class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> net_trust(n + 1, 0);

        for (const vector<int>& edge : trust) {
            net_trust[edge[0]]--;
            net_trust[edge[1]]++;
        }

        for (int i = 0; i < n + 1; i++) {
            if (net_trust[i] == n - 1) return i;
        }

        return -1;
    }
};