class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = ""

        def isRepeatingChar(char):
            return (len(result) >= 2 and 
                result[-1] == char and 
                result[-2] == char)
        
        max_heap = []
        if a > 0: heapq.heappush_max(max_heap, (a, 'a'))
        if b > 0: heapq.heappush_max(max_heap, (b, 'b'))
        if c > 0: heapq.heappush_max(max_heap, (c, 'c'))

        while max_heap:
            count, ch = heapq.heappop_max(max_heap)

            if isRepeatingChar(ch):
                if not max_heap: 
                    break
                next_count, next_char = heapq.heappop_max(max_heap)
                result += next_char
                next_count -= 1
                if next_count > 0: 
                    heapq.heappush_max(max_heap, (next_count, next_char))
            else:
                result += ch
                count -= 1
            if count > 0: 
                heapq.heappush_max(max_heap, (count, ch))

        return result