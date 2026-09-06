class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_edges = defaultdict(int)
        out_edges = defaultdict(int)
        for truster, trustee in trust:
            in_edges[trustee] += 1
            out_edges[truster] += 1
        
        for i in range(1, n + 1):
            if in_edges[i] == n - 1 and out_edges[i] == 0:
                return i
        return -1