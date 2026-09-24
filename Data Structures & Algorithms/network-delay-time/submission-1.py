class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for src, dest, cost in times:
            adj_list[src].append((dest, cost))

        shortest = {}
        min_heap = [(0, k)]
        while min_heap:
            curr_cost, curr_node = heapq.heappop(min_heap)
            if curr_node in shortest:
                continue
            shortest[curr_node] = curr_cost

            for neighbor_node, neighbor_cost in adj_list[curr_node]:
                if neighbor_node not in shortest:
                    heapq.heappush(min_heap, 
                        (neighbor_cost + curr_cost, neighbor_node))
        return -1 if n != len(shortest) else max(shortest.values())





