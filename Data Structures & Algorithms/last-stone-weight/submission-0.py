# You are given an array of integers stones where stones[i] represents the weight of the ith stone.

# Simulation Step Criteria
# At each step we choose the two heaviest stones, with weight x and y and smash them togethers

# If x == y, both stones are destroyed

# If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

# idea: min_heap
# - the root is always the current heaviest
# - x, y: get the root x2 
#     - compare the two
#         - if == then we are done for this iteration
#         - if not equal, heappush the left over stone

# Stone  is always positive
# There is always at least 1 stone

# Base case: 1 stone

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x, y = heapq.heappop_max(stones), heapq.heappop_max(stones)
        
            if x > y:
                heapq.heappush_max(stones, x - y)
            
        return stones[0] if len(stones) == 1 else 0



