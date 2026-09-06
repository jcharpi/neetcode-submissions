class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        net_trust = defaultdict(int)
        for truster, trustee in trust:
            net_trust[trustee] += 1
            net_trust[truster] -= 1
        
        for i in range(1, n + 1):
            if net_trust[i] == n - 1:
                return i
        return -1