class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        stack = [] # [temp, index]

        for currIndex, currValue in enumerate(temperatures):
            print(f"{currIndex}, {currValue}")
            while stack and stack[-1][0] < currValue:
                stackValue, stackIndex = stack.pop()
                res[stackIndex] = currIndex-stackIndex
            stack.append([currValue, currIndex])
        return res