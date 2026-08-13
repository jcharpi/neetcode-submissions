class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int two_back = cost[0], one_back = cost[1];
        for (int i = 2; i < ssize(cost); i++) {
            int curr = cost[i] + min(one_back, two_back);
            two_back = one_back;
            one_back = curr;
        }
        return min(one_back, two_back);
    }
};
