class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonically decreasing stack
        # [30]
        # [0, 0, 0, 0, 0, 0, 0]
        # [38]
        # [1, 0, 0, 0, 0, 0, 0]
        # 38 > 30 so pop 30. At index of 30: index of 38 - 30 (1)

        stack = []
        out = [0 for i in range(len(temperatures))]
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                poppedTempIndex = stack.pop()
                out[poppedTempIndex] = i - poppedTempIndex
            stack.append(i)
        return out
            