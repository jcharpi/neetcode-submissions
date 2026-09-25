class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Given
        #     - undirected weighted graph of n nodes
        #     - represented by an edge list where edges[i] = [a, b]
        #     -- TODO: make adj list from edge list
        #     -- probability of success of traversing that edge succProb[i].

        # Goal
        #     - Given start and end, find path w/ max probability of success to go from start to end
        #     - return probability of success
        #     - if no path, return 0

        # DSA
        # - Dijkstra but lowest cost == highest probability
        # -- Each traversal multiplies probability so far * curr probability

        adj_list = defaultdict(list)
        for i in range(len(edges)):
            src, dest, cost = edges[i][0], edges[i][1], succProb[i]
            adj_list[src].append((dest, cost))
            adj_list[dest].append((src, cost))

        visited = {}
        max_heap = [(1, start_node)]
        while max_heap:
            curr_prob, curr_node = heapq.heappop_max(max_heap)
            if curr_node in visited:
                continue
            visited[curr_node] = curr_prob

            for neighbor_node, neighbor_prob in adj_list[curr_node]:
                if neighbor_node not in visited:
                    heapq.heappush_max(max_heap, ((neighbor_prob * curr_prob), neighbor_node))
        return 0 if end_node not in visited else visited[end_node]



