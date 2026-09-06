class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_edges, out_edges = [0 for i in range(n + 1)], [0 for i in range(n + 1)]
        for truster, trustee in trust:
            in_edges[trustee] += 1
            out_edges[truster] += 1
        
        for index, (person_in, person_out) in enumerate(list(zip(in_edges, out_edges))):
            if person_in == n - 1 and person_out == 0:
                return index
        return -1