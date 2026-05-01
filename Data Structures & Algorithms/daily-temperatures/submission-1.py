class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 3
        # 0 0 0 0

        # 3, 1
        # 0 0 0 0

        # 3, 1, 1
        # 0 0 0 0


        # 3, 1, 2
        # pop 1
        # 0, 0, 1, 0
        
        # 3, 2
        # pop 1
        # 0, 2, 1, 0

        out = [0 for i in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                stackPoppedIndex = stack.pop()
                out[stackPoppedIndex] = i - stackPoppedIndex
            stack.append(i)
                 
        return out
