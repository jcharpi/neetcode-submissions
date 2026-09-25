class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = defaultdict(list)
        for i in range(len(edges)):
            src, dest, prob = edges[i][0], edges[i][1], succProb[i]
            adj_list[src].append((dest, prob))
            adj_list[dest].append((src, prob))

        shortest = {}
        max_heap = [(1, start_node)]
        while max_heap:
            curr_prob, curr_node = heapq.heappop_max(max_heap)
            if curr_node in shortest:
                continue
            shortest[curr_node] = curr_prob

            for neighbor_node, neighbor_prob in adj_list[curr_node]:
                if neighbor_node not in shortest:
                    heapq.heappush_max(max_heap, ((neighbor_prob * curr_prob), neighbor_node))
        return 0 if end_node not in shortest else shortest[end_node]
