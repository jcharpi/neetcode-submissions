class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        two_back, one_back = cost[0], cost[1]
        for i in range(2, len(cost)):
            curr = cost[i] + min(two_back, one_back)
            two_back, one_back = one_back, curr
        return min(two_back, one_back)