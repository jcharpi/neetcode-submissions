class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Given
        # - 2D integer array points
        # - points[i] = xi, yi
        # - cost of connecting two points is |xi-xj| + |yi - yj|
        
        # Goal
        # - return min cost to connect all points together without cycles
        # -- Min spanning tree
        # -- Prim

        # DSA
        # - Prims where the cost is the manhattan distance
        # - how do we track this? 
        # -- we are given a point's src; can we make an adjacency list?
        # -- do we need an adj list? usually this represents src: (dest, cost)
        # --- we can create the edges by calculating cost between everything
        def get_cost(src, dest):
            src_x, src_y = points[src]
            dest_x, dest_y = points[dest]
            return abs(src_x - dest_x) + abs(src_y - dest_y)

        n = len(points)
        adj_list = { i : [] for i in range(n) }
        for i in range(n):
            for j in range(i + 1, n):
                dist = get_cost(i, j)
                adj_list[i].append((j, dist))
                adj_list[j].append((i, dist))

        min_cost = 0
        min_heap = []
        visited = set()
        for dest, cost in adj_list[0]:
            heapq.heappush(min_heap, [cost, 0, dest])
        
        visited.add(0)
        while min_heap:
            cost, src, dest = heapq.heappop(min_heap)
            if dest in visited:
                continue
            visited.add(dest)
            min_cost += cost

            for next_dest, next_cost in adj_list[dest]:
                if next_dest not in visited:
                    heapq.heappush(min_heap, [next_cost, dest, next_dest])
        return min_cost