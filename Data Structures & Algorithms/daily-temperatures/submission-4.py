class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmest = []
        out = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):            
            while warmest and temp > temperatures[warmest[-1]]:
                day_index = warmest.pop()
                out[day_index] = i - day_index
            
            warmest.append(i)
            print(warmest)

        return out

#                     x
# 30, 38, 30, 36, 35, 40, 28
# 1,  0,  1,  2,  1,  0,  0

# [1, 3, 4]
