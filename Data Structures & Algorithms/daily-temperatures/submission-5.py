class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waiting = []
        out = [0] * len(temperatures)
        for curr_day_index, temp in enumerate(temperatures):            
            while waiting and temp > temperatures[waiting[-1]]:
                prev_day_index = waiting.pop()
                out[prev_day_index] = curr_day_index - prev_day_index
            
            waiting.append(curr_day_index)

        return out
