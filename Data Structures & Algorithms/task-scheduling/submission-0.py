class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = list(Counter(tasks).values())
        q = deque()
        heapq.heapify_max(task_counts)

        time = 0
        while task_counts or q:
            time += 1

            if task_counts:
                count = heapq.heappop_max(task_counts)
                if count - 1 > 0:
                    q.append((count - 1, time + n))
                
            if q and q[0][1] == time:
                heapq.heappush_max(task_counts, q.popleft()[0])
            
        return time

