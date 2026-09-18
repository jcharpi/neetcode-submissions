class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank, start_index = 0, 0

        if sum(gas) < sum(cost):
            return -1
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start_index = i + 1
                tank = 0
            
        return start_index



        