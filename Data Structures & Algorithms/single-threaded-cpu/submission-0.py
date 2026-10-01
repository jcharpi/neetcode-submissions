class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pending, available = [], []
        for i, (enqueue_time, processing_time) in enumerate(tasks):
            heapq.heappush(pending, (enqueue_time, processing_time, i))

        clock, out = 0, []
        while pending or available:
            # pending enqueue time <= clock; we can add it
            while pending and pending[0][0] <= clock:
                enqueue_time, processing_time, i = heapq.heappop(pending)
                heapq.heappush(available, (processing_time, i))
            
            if not available:
                clock = pending[0][0]
                continue
            
            processing_time, i = heapq.heappop(available)
            clock += processing_time
            out.append(i)
        return out
