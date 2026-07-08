class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        waiting = []
        for i, temp in enumerate(temperatures):
            while waiting and temp > temperatures[waiting[-1]]:
                resolved_temp_index = waiting.pop()
                out[resolved_temp_index] = i - resolved_temp_index
            waiting.append(i)
        return out