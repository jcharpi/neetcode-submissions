class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for flight_src, flight_dest, flight_cost in flights:
            adj_list[flight_src].append((flight_dest, flight_cost))
        
        shortest, min_heap = {}, [(0, src, 0)]
        max_flights = k + 1
        while min_heap:
            curr_cost, curr_dest, curr_flights = heapq.heappop(min_heap)

            if curr_dest == dst:
                return curr_cost

            if curr_dest in shortest and shortest[curr_dest] <= curr_flights:
                continue
            shortest[curr_dest] = curr_flights

            if curr_flights == max_flights:
                continue

            for neighbor_dest, neighbor_cost in adj_list[curr_dest]:
                heapq.heappush(min_heap, (curr_cost + neighbor_cost, neighbor_dest, curr_flights + 1))

        return -1
